import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np

columns = {"potential_flux": 2,
           "absorbed_flux": 3,
           "cos_factor": 4,
           "shadow_losses": 5,
           }

txtfiles = glob.glob('export/raw/*.txt')

df = pd.read_csv(txtfiles[0], sep='\s+',names=range(47))
fname = os.path.basename(txtfiles[0]).split(".")[0]
angles = df.loc[df[1] == 'Sun'][3]  # set 4 for longitudinal
eff = df.loc[df[0] == 'absorber',[23]] # Overall effficiency, add [23,24] for error

for i in columns.keys():
    eff[i] = df[0].iloc[angles.index + columns.get(i)].astype('float').values
colnames = ["efficiency"] + [*columns.keys()]
eff = eff.set_index(angles.values)
eff.columns = colnames

for i in columns.keys():
    plt.plot(eff[i])
    plt.title(fname)
    plt.ylabel(i.replace("_"," ").title())
    plt.show()


# plt.plot(angle_eff_err["efficiency"])
# plt.plot(angle_eff_err["min"])
# plt.plot(angle_eff_err["max"])
# # def plot_angle_efficiency(series):
# #     plt.plot(series)
# #     plt.title(series.name)
# #     plt.ylabel("Optical efficiency")
# #     if series.name == "transversal":
# #         plt.xticks(np.arange(30,145,10))
# #         plt.xlim(40, 140)
# #         plt.xlabel('Azimuth (90$\degree$=nornal incidence)')
# #     else:
# #         plt.xlabel(xlabel="Zenith (0$\degree$=nornal incidence)")
# #     plt.savefig(f'plots/{series.name}.png')
# #     plt.show()
