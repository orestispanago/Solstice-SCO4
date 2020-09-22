import pandas as pd
from traces import Transversal, Longitudinal
import matplotlib.pyplot as plt
import numpy as np

# transversal = Transversal(45,135,1,10000)
# transversal.run()
# transversal.export_obj()
# transversal.export_vtk()


# longitudinal = Longitudinal(0, 25, 0.5,10000)
# longitudinal.run()
# longitudinal.export_obj()
# longitudinal.export_vtk()

# df = pd.read_csv("raw/transversal.txt",sep='\s+',names=range(47))


# angles = df.loc[df[1]=='Sun'][3] # set 4 for longitudinal
# eff = df.loc[df[0]=='absorber'][23]
# angle_eff = pd.Series(eff.values,index=angles.values)
# # angle_eff.plot()


# plt.plot(angle_eff)
# plt.title("Transversal")
# plt.ylabel("Optical efficiency")
# plt.xticks(np.arange(30,145,10))
# plt.xlim(40, 140)
# plt.xlabel('Azimuth (90$\degree$=nornal incidence)')
# plt.savefig('plots/tranvsersal.png')

df = pd.read_csv("raw/longitudinal.txt",sep='\s+',names=range(47))
angles = df.loc[df[1]=='Sun'][4] # set 4 for longitudinal
eff = df.loc[df[0]=='absorber'][23]
angle_eff = pd.Series(eff.values,index=angles.values)


plt.plot(angle_eff)
plt.title("Longitudinal")
plt.ylabel("Optical efficiency")
plt.xlabel('Zenith (0$\degree$=nornal incidence)')
plt.savefig('plots/longitudinal.png')