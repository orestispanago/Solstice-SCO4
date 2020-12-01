import os
import subprocess
import pandas as pd
from setup import check_installation


columns = {
           "potential_flux": 2,
           "absorbed_flux": 3,
           "cos_factor": 4,
           "shadow_losses": 5,
           "missing_losses": 6,
           # "reflectivity_losses": 7,
           # "absorptivity_losses": 8
           }


df = pd.read_csv("radiation/sol.csv", index_col="t", parse_dates=True)


df["az"] = df["az"] - 90
df["zen"] = 90 - df["alt"]

days = [group[1] for group in df.groupby(df.index.date)]

a = days[0]


check_installation()
receiver = os.path.join(os.getcwd(), "geometries", "receiver.yaml")
geometry = os.path.join(os.getcwd(), "geometries", "ideal-plain.yaml")
outfile = "test.txt"
with open(outfile, "w") as f:
    for az,zen in zip(a["az"], a["zen"]):
        pair = f"{az:.1f},{zen:.1f}"
        cmd = f"solstice -D {pair} -n 10000 -v -R {receiver} {geometry}".split()
        subprocess.run(cmd, stdout=f)


def read(fname):
    df = pd.read_csv(fname, sep='\s+', names=range(47))
    df_out = df.loc[df[1] == 'Sun', [3]]  # azimuth
    df_out.columns = ["azimuth"]
    df_out["zenith"] = df.loc[df[1] == 'Sun', [4]] # zenith
    df_out["efficiency"] = df.loc[df[0] == 'absorber', [23]].values  # Overall effficiency, add [23,24] for error
    for key in columns.keys():
        df_out[key] = df[0].iloc[df_out.index + columns.get(key)].astype('float').values
    return df_out

day1 = read(outfile)
day1["time"] = a.index
day1 = day1.set_index("time")

day1["absorbed_flux"].plot()
