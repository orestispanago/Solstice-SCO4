import os
import pandas as pd
import subprocess
from io import StringIO
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
from directions import Annual
import mod_geometry

def read(fname):
    columns = {
           "potential_flux": 2,
           "absorbed_flux": 3,
           "cos_factor": 4,
           "shadow_losses": 5,
           "missing_losses": 6,
           # "reflectivity_losses": 7,
           # "absorptivity_losses": 8
    }
    df = pd.read_csv(fname, sep='\s+', names=range(47))
    df_out = df.loc[df[1] == 'Sun', [3]]  # azimuth
    df_out.columns = ["azimuth"]
    df_out["zenith"] = df.loc[df[1] == 'Sun', [4]] # zenith
    df_out["efficiency"] = df.loc[df[0] == 'entity_all.absorber', [23]].values  # Overall effficiency, add [23,24] for error
    for key in columns.keys():
        df_out[key] = df[0].iloc[df_out.index + columns.get(key)].astype('float').values
    return df_out

def plot_calendar_heatmap(dfin, col, freq="1min", units="", folder="calendar-heatmaps"):
    df = dfin.resample(freq).mean().dropna()
    df["Time, UTC"] = df.index.time
    df["Date"] = df.index.date
    df.reset_index(inplace=True)
    df = df.pivot("Time, UTC","Date", col)
    fig, ax = plt.subplots(figsize=(25,6))
    cbar_label = col.replace("_"," ").title() + units
    ax = sns.heatmap(df, cmap="jet",cbar_kws={'label': cbar_label})
    plt.tight_layout()
    plt.savefig(f"{folder}/{col}.png")
    plt.show()

def run_chunks_to_df(direction):
    """ Runs Direction and pipes output to dataframe """
    df_list = []
    # Solstice cannot take too long string of angle arguments, so split into chunks
    for i in tqdm(range(0, len(direction.angle_pairs), 20)):
        chunk = direction.angle_pairs[i:i + 20]
        chunk = ":".join(chunk)
        cmd = f'solstice -D {chunk} -n {direction.rays} -v -R {direction.receiver} {direction.geometry_path}'.split()
        a = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        b = StringIO(a.communicate()[0].decode('utf-8'))
        df = read(b)
        df_list.append(df)
    return pd.concat(df_list)

def run_annual(direction, df):
    receiver = "geometries/receiver_annual.yaml"
    df_list = []
    for pair, dni in tqdm(zip(direction.angle_pairs, df["DNI"]), total=len(df)):
        mod_geometry.set_dni(direction.geometry_path, dni)
        cmd = f'solstice -D {pair} -n {direction.rays} -v -R {receiver} {direction.geometry_path}'.split()
        a = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        b = StringIO(a.communicate()[0].decode('utf-8'))
        df = read(b)
        df_list.append(df)
    return pd.concat(df_list)

df = pd.read_csv("radiation/solar.csv", index_col="t", parse_dates=True)
df = df.loc[(df[['DNI']] != 0).all(axis=1)] # drop zeros
pairs = [f"{az:.1f},{zen:.1f}" for az, zen in zip(df["az"], df["zen"])]

annual = Annual(10000, pairs, "ideal", "annual-tilt20.yaml")
annual_df = run_annual(annual, df)

annual_df["time"] = df.index
annual_df = annual_df.set_index("time")
annual_df.to_csv(annual.csv_path)

annual_df = pd.read_csv(annual.csv_path, index_col="time", parse_dates=True)

os.makedirs(annual.plots_dir)
plot_calendar_heatmap(annual_df, "efficiency", folder=annual.plots_dir)


# annual1 = annual.resample("D").mean()
# annual1["absorbed_flux"].plot()

plot_calendar_heatmap(annual_df, "efficiency", folder=annual.plots_dir)
plot_calendar_heatmap(annual_df, "cos_factor", folder=annual.plots_dir)
plot_calendar_heatmap(annual_df, "absorbed_flux", folder=annual.plots_dir)
plot_calendar_heatmap(annual_df, "missing_losses", folder=annual.plots_dir)
plot_calendar_heatmap(annual_df, "shadow_losses", folder=annual.plots_dir)
plot_calendar_heatmap(annual_df, "potential_flux", folder=annual.plots_dir)
