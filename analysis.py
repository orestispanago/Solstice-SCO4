import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from run import transversal


columns = {"potential_flux": 2,
           "absorbed_flux": 3,
           "cos_factor": 4,
           "shadow_losses": 5
           }

df = pd.read_csv(transversal.rawfile, sep='\s+',names=range(47))
angles = df.loc[df[1] == 'Sun', [transversal.sun_col]]  # set 4 for longitudinal
eff = df.loc[df[0] == 'absorber',[23]] # Overall effficiency, add [23,24] for error

for i in columns.keys():
    eff[i] = df[0].iloc[angles.index + columns.get(i)].astype('float').values
colnames = ["efficiency"] + [*columns.keys()]
eff = eff.set_index(angles[3].values)
eff.columns = colnames


for i in colnames:
    plt.plot(eff[i])
    plt.title(transversal.name)
    plt.ylabel(i.replace("_"," ").title())
    plt.xticks(np.arange(30,145,10))
    plt.xlim(40, 140)
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
