import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np



txtfiles = glob.glob('export/raw/*.txt')

df = pd.read_csv(txtfiles[1], sep='\s+',names=range(47))
fname = os.path.basename(txtfiles[1]).split(".")[0]
angles = df.loc[df[1] == 'Sun'][3]  # set 4 for longitudinal
shadow = df[0].iloc[angles.index+5].astype('float')
absorbed_flux = df[0].iloc[angles.index+3].astype('float')
eff = df.loc[df[0] == 'absorber',[23]] # Add [23,24] for error
eff['shadow'] = shadow.values
eff['absorbed'] = absorbed_flux.values
angle_df = pd.DataFrame(eff.values, index=angles.values, columns=["efficiency", "shadow","absorbed"])
angle_df.name = fname


plt.plot(angle_df["shadow"])
plt.title(angle_df.name)
plt.ylabel("Shadow losses (W)")
plt.show()

plt.plot(angle_df["absorbed"])
plt.title(angle_df.name)
plt.ylabel("Absorbed flux by receiver (W)")
plt.show()

plt.plot(angle_df["efficiency"])
plt.title(angle_df.name)
plt.ylabel("Optical efficieicy")
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
