import os
import numpy as np
import subprocess
import utils
from io import StringIO
import pandas as pd

CWD = os.getcwd()
receiver = os.path.join(CWD, "geometries", "receiver.yaml")


class Trace():

    def __init__(self, min_angle, max_angle, step, rays, geometry, name):
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.step = step
        self.rays = rays
        self.angles = np.arange(min_angle, max_angle + 1, step).tolist()
        self.name = name
        self.title = self.name + " " + geometry.split(".")[0]
        self.geometry = os.path.join(CWD, "geometries", geometry)
        self.exp_dir = os.path.join(CWD, 'export', geometry.split(".")[0])
        self.shape_dir = os.path.join(self.exp_dir, "shapes")
        self.rawfile = os.path.join(self.exp_dir, 'raw', self.name + ".txt")
        self.meanfile = os.path.join(self.exp_dir, 'raw', self.name + "-means.csv")
        self.df = None

    def run(self):
        utils.mkdir_if_not_exists(os.path.dirname(self.rawfile))
        with open(self.rawfile, 'w') as f:
            # Solstice cannot take too long string of angle arguments, so split into chunks
            for i in range(0, len(self.angle_pairs), 50):
                chunk = self.angle_pairs[i:i + 50]
                chunk = ":".join(chunk)
                cmd = f'solstice -D {chunk} -n {self.rays} -v -R {receiver} {self.geometry}'.split()
                subprocess.run(cmd, stdout=f)

    def run_set_df(self):
        """ Runs Trace and pipes output to dataframe, sets df as Trace attr """
        # Solstice cannot take too long string of angle arguments, so split into chunks
        df_list = []
        for i in range(0, len(self.angle_pairs), 50):
            chunk = self.angle_pairs[i:i + 50]
            chunk = ":".join(chunk)
            cmd = f'solstice -D {chunk} -n {self.rays} -v -R {receiver} {self.geometry}'.split()
            a = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            b = StringIO(a.communicate()[0].decode('utf-8'))
            df = pd.read_csv(b, sep='\s+', names=range(47))
            df_list.append(df)
        df_out = pd.concat(df_list)
        self.df = df_out

    def export_vtk(self, nrays=100000):
        for pair in [self.angle_pairs[0], self.angle_pairs[-1]]:
            pair_str = pair.replace(',', '_')
            fname = f"{self.name}_{pair_str}.vtk"
            utils.mkdir_if_not_exists(self.shape_dir)
            vtkpath = os.path.join(self.exp_dir, "shapes", fname)
            cmd = f'solstice  -n {nrays} -p default -t1 -D {pair} -R {receiver} {self.geometry}'.split()
            with open(vtkpath, 'w') as f:
                subprocess.run(cmd, stdout=f)
            utils.del_first_line(vtkpath)

    def export_obj(self):
        for pair in [self.angle_pairs[0], self.angle_pairs[-1]]:
            pair_str = pair.replace(',', '_')
            fname = f"{self.name}_{pair_str}.obj"
            utils.mkdir_if_not_exists(self.shape_dir)
            objpath = os.path.join(self.shape_dir, fname)
            cmd = f'solstice  -n 100 -g format=obj -t1 -D {pair} -R {receiver} {self.geometry}'.split()
            with open(objpath, 'w') as f:
                subprocess.run(cmd, stdout=f)

    def export_heat(self, nrays=1000000):
        receiver_heat = os.path.join(CWD, "geometries", "heatmap", "receiver.yaml")
        geometry_heat = os.path.join(CWD, "geometries", "heatmap", "geometry.yaml")
        for pair in [self.angle_pairs[0], self.angle_pairs[-1]]:
            pair_str = pair.replace(',', '_')
            fname = f"{self.name}_{pair_str}_heatmap.vtk"
            heat_path = os.path.join(self.exp_dir, "shapes", fname)
            cmd = f'solstice  -n {nrays} -v -t16 -D {pair} -R {receiver_heat} {geometry_heat}'.split()
            with open(heat_path, 'w') as f:
                subprocess.run(cmd, stdout=f)
            utils.del_until(heat_path)


class Transversal(Trace):
    def __init__(self, min_angle, max_angle, step, rays, geometry):
        super().__init__(min_angle, max_angle, step, rays, geometry, name=self.__class__.__name__)
        self.angle_pairs = [f"{a:.1f},0" for a in self.angles]
        self.sun_col = 3  # sun direction column in txt output file
        self.xlabel = "$\\theta_z$ $(\degree)$, 0$\degree$=Normal Incidence"


class Longitudinal(Trace):
    def __init__(self, min_angle, max_angle, step, rays, geometry):
        super().__init__(min_angle, max_angle, step, rays, geometry, name=self.__class__.__name__)
        self.angle_pairs = [f"90,{a:.1f}" for a in self.angles]
        self.sun_col = 4  # sun direction column in txt output file
        self.xlabel = "$\\theta_z$ $(\degree)$, 0$\degree$=Normal Incidence"
