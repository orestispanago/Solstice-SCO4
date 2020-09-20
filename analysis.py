import pandas as pd
from traces import Transversal, Longitudinal

transversal = Transversal(45,135,1,10000)
transversal.run()
transversal.export_obj()
transversal.export_vtk()


longitudinal = Longitudinal(0, 25, 1,10000)
longitudinal.run()
longitudinal.export_obj()
longitudinal.export_vtk()

df = pd.read_csv("raw/transversal.txt",sep='\s+',names=range(47))

step=14 # 12 for plain, 14 for aux surface
angle = df.loc[0::step,3].values # first_row::step,column
eff_side1_df = df.loc[9::step, 23].values
eff_side2_df = df.loc[9::step, 45].values

angle_eff = pd.DataFrame({'side1':eff_side1_df,'side2':eff_side2_df}, index=angle)  # 1st row as the column names
angle_eff['total_eff'] = angle_eff['side1'] + angle_eff['side2']
angle_eff['total_eff'].plot()
