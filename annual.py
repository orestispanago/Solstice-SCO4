import os
import pandas as pd
import subprocess
from io import StringIO
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from directions import Annual
import mod_geometry

sns.set_theme()

params = {'figure.figsize': (14, 4),
          'axes.titlesize': 20,
          'axes.titleweight': 'bold',
          'axes.labelsize': 20,
          'axes.labelweight': 'bold',
          'xtick.labelsize': 20,
          'ytick.labelsize': 20,
          'font.weight': 'bold',
          'font.size': 25,
          'legend.fontsize': 16,
          'savefig.format': 'png',
          # 'savefig.dpi': 300.0,
           'figure.constrained_layout.use': True,
          }
plt.rcParams.update(params)


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

def plot_calendar_heatmap(dfin, col, freq="1min",cbar_label=None, units="", 
                          folder="calendar-heatmaps"):
    df = dfin.resample(freq).mean().dropna()
    df["Time, UTC"] = df.index.time
    df["Date"] = df.index.date
    df.reset_index(inplace=True)
    df = df.pivot("Time, UTC","Date", col)
    fig, ax = plt.subplots(figsize=(30,8))
    if not cbar_label:
        cbar_label = col.replace("_"," ").title() + units
    ax = sns.heatmap(df, cmap="jet",cbar_kws={'label': cbar_label}, 
                     xticklabels=31, yticklabels=30)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    # plt.tight_layout()
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


df = pd.read_csv("radiation/solar_all.csv", index_col="t", parse_dates=True)
df = df.loc[df["zen"]<=90]
df = df.loc[(df[['DNI']] > 0).all(axis=1)] # drop zeros
pairs = [f"{az:.1f},{zen:.1f}" for az, zen in zip(df["az"], df["zen"])]

annual = Annual(10000, pairs, "ideal", "annual-tilt38.yaml")
annual_df = run_annual(annual, df)

annual_df["time"] = df.index
annual_df = annual_df.set_index("time")
annual_df.to_csv(annual.csv_path.split(".")[0]+"all.csv")

annual_df1 = pd.read_csv(annual.csv_path, index_col="time", parse_dates=True)

# os.makedirs(annual.plots_dir)
# plot_calendar_heatmap(annual_df, "efficiency", folder=annual.plots_dir)
# plot_calendar_heatmap(annual_df, "cos_factor", folder=annual.plots_dir)
# plot_calendar_heatmap(annual_df, "absorbed_flux", folder=annual.plots_dir)
# plot_calendar_heatmap(annual_df, "missing_losses", folder=annual.plots_dir)
# plot_calendar_heatmap(annual_df, "shadow_losses", folder=annual.plots_dir)
# plot_calendar_heatmap(annual_df, "potential_flux", folder=annual.plots_dir)


# annual1 = annual_df1.resample("D").mean()
# annual1["absorbed_flux"].plot()
# annual1["azimuth"].plot()
# annual1["zenith"].plot()
# annual1["absorbed_flux"].plot()

# df1 = df.resample("D").mean()
# df1["az"].plot()


# plot_calendar_heatmap(df, "DNI", folder=annual.plots_dir, cbar_label=r"DNI $\frac{W}{m^2}$")
# plot_calendar_heatmap(df, "GHI", folder=annual.plots_dir, cbar_label=r"GHI $\frac{W}{m^2}$")
# plot_calendar_heatmap(df, "DHI", folder=annual.plots_dir, cbar_label=r"DHI $\frac{W}{m^2}$")
# plot_calendar_heatmap(df, "az", folder=annual.plots_dir, cbar_label=r"$\theta_{az}$ $( \degree)$")
plot_calendar_heatmap(df, "zen", folder=annual.plots_dir, cbar_label=r"$\theta_{z}$ $( \degree)$")
