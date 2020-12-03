import os
import pandas as pd
import export
import subprocess
from io import StringIO
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns


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
    df_out["efficiency"] = df.loc[df[0] == 'absorber', [23]].values  # Overall effficiency, add [23,24] for error
    for key in columns.keys():
        df_out[key] = df[0].iloc[df_out.index + columns.get(key)].astype('float').values
    return df_out

class Annual:
    def __init__(self, angle_pairs, geometry_path, receiver, rays):
        self.rays=rays
        self.angle_pairs=angle_pairs
        self.geometry_path=geometry_path
        self.receiver=receiver

def run_to_df(direction):
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

df = pd.read_csv("radiation/sol.csv", index_col="t", parse_dates=True)

df["az"] = df["az"] - 90
df["zen"] = 90 - df["alt"]

receiver = os.path.join(os.getcwd(), "geometries", "receiver.yaml")
geometry = os.path.join(os.getcwd(), "geometries", "ideal-plain.yaml")
pairs = [f"{az:.1f},{zen:.1f}" for az, zen in zip(df["az"], df["zen"])]
a = Annual(pairs, geometry, receiver, 10000)

# annual_df = run_to_df(a)
# annual_df["time"] = df.index
# annual_df = annual_df.set_index("time")

annual = pd.read_csv("annual.csv", index_col="time", parse_dates=True)


def plot_calendar_heatmap(dfin, col, freq="1min", units=""):
    df = dfin.resample(freq).mean().dropna()
    df["Time, UTC"] = df.index.time
    df["Date"] = df.index.date
    df.reset_index(inplace=True)
    df = df.pivot("Time, UTC","Date", col)
    fig, ax = plt.subplots(figsize=(25,6))         # Sample figsize in inches
    cbar_label = col.replace("_"," ").title()
    cbar_label += units
    ax = sns.heatmap(df, cmap="jet",cbar_kws={'label': cbar_label})
    plt.tight_layout()
    plt.savefig("heatmap.png")
    plt.show()

plot_calendar_heatmap(annual, "absorbed_flux", units=" (W)")


annual1 = annual.resample("D").mean()
annual1["absorbed_flux"].plot()
