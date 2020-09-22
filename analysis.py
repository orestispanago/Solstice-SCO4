import pandas as pd
from traces import Transversal, Longitudinal
import matplotlib.pyplot as plt
import numpy as np


def read_angle_eff(trace):
    df = pd.read_csv(trace.outfile, sep='\s+',names=range(47))
    angles = df.loc[df[1] == 'Sun'][trace.sun_col]  # set 4 for longitudinal
    eff = df.loc[df[0] == 'absorber'][23].dropna()
    angle_eff = pd.Series(eff.values, index=angles.values, name=trace.name)
    return angle_eff


def plot_angle_efficiency(series):
    plt.plot(series)
    plt.title(series.name.capitalize())
    plt.ylabel("Optical efficiency")
    if series.name == "transversal":
        plt.xticks(np.arange(30,145,10))
        plt.xlim(40, 140)
        plt.xlabel('Azimuth (90$\degree$=nornal incidence)')
    else:
        plt.xlabel(xlabel="Zenith (0$\degree$=nornal incidence)")
    plt.savefig(f'plots/{series.name}.png')
    plt.show()



transversal = Transversal(45, 135, 1, 10000)
transversal.run()
transversal.export_obj()
transversal.export_vtk()

longitudinal = Longitudinal(0, 25, 0.5, 10000)
longitudinal.run()
longitudinal.export_obj()
longitudinal.export_vtk()


long = read_angle_eff(longitudinal)
transv = read_angle_eff(transversal)

plot_angle_efficiency(long)
plot_angle_efficiency(transv)

# command to export heatmap vtk
# solstice -n 1000000 -v -t1 -D 45.0,0 -R /home/orestis/Projects/Solstice-SCO4/geometry/receiver.yaml /home/orestis/Projects/Solstice-SCO4/geometry/geometry1.yaml > heatmap.vtk
# TODO add seoarate yaml file for heatmap or solve nan issue