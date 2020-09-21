import pandas as pd
from traces import Transversal, Longitudinal

transversal = Transversal(45,135,1,10000)
transversal.run()
transversal.export_obj()
transversal.export_vtk()


# longitudinal = Longitudinal(0, 25, 1,10000)
# longitudinal.run()
# longitudinal.export_obj()
# longitudinal.export_vtk()

df = pd.read_csv("raw/transversal.txt",sep='\s+',names=range(47))


angles = df.loc[df[1]=='Sun'][3] # set 4 for longitudinal
eff = df.loc[df[0]=='absorber'][23]
angle_eff = pd.Series(eff.values,index=angles.values)
angle_eff.plot()