import numpy as np
import os
import subprocess
import utils

CWD = os.getcwd()
# exp_dir = os.path.join(CWD, 'export', 'ideal')
shapes_dir = os.path.join(CWD, 'export', "shapes")
# geometry = os.path.join(CWD, "geometry", "geometry_glass.yaml")
receiver = os.path.join(CWD, "geometry", "receiver.yaml")


class Trace():

    def __init__(self, min_angle, max_angle, step, rays, geometry, name):
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.step = step
        self.rays = rays
        self.angles = np.arange(min_angle, max_angle + 1, step).tolist()
        self.name = name
        self.geometry = os.path.join(CWD, "geometry", geometry)
        self.exp_dir = os.path.join(CWD, 'export', geometry.split(".")[0])
        self.rawfile = os.path.join(self.exp_dir, 'raw', self.name + ".txt")
        
    def run(self):
        with open(self.rawfile, 'w') as f:
            # Solstice cannot take too long string of angle arguments, so split into chunks
            for i in range(0, len(self.angle_pairs), 50):
                chunk = self.angle_pairs[i:i + 50]
                chunk = ":".join(chunk)
                cmd = f'solstice -D {chunk} -n {self.rays} -v -R {receiver} {self.geometry}'.split()
                subprocess.run(cmd, stdout=f)

    def export_vtk(self, nrays=100):
        for pair in [self.angle_pairs[0], self.angle_pairs[-1]]:
            pair_str = pair.replace(',', '_')
            fname = f"{self.name}_{pair_str}.vtk"
            vtkpath = os.path.join(self.exp_dir, "shapes", fname)
            cmd = f'solstice  -n {nrays} -p default -t1 -D {pair} -R {receiver} {self.geometry}'.split()
            with open(vtkpath, 'w') as f:
                subprocess.run(cmd, stdout=f)
            utils.del_first_line(vtkpath)

    def export_obj(self):
        for pair in [self.angle_pairs[0], self.angle_pairs[-1]]:
            pair_str = pair.replace(',', '_')
            fname = f"{self.name}_{pair_str}.obj"
            objpath = os.path.join(self.exp_dir,"shapes", fname)
            cmd = f'solstice  -n 100 -g format=obj -t1 -D {pair} -R {receiver} {self.geometry}'.split()
            with open(objpath, 'w') as f:
                subprocess.run(cmd, stdout=f)
                
    def export_heat(self, nrays=1000000):
        receiver_heat = os.path.join(CWD, "geometry", "heatmap", "receiver.yaml")
        geometry_heat = os.path.join(CWD, "geometry", "heatmap", "geometry.yaml")  # Path needs to be set in file

        for pair in [self.angle_pairs[0], self.angle_pairs[-1]]:
            pair_str = pair.replace(',', '_')
            fname = f"{self.name}_{pair_str}_heatmap.vtk"
            heat_path = os.path.join(shapes_dir, fname)
            cmd = f'solstice  -n {nrays} -v -t16 -D {pair} -R {receiver_heat} {geometry_heat}'.split()
            with open(heat_path, 'w') as f:
                subprocess.run(cmd, stdout=f)
            utils.del_until(heat_path)
                
class Transversal(Trace):
    def __init__(self, min_angle, max_angle, step, rays, geometry):
        super().__init__(min_angle, max_angle, step, rays, geometry, name=self.__class__.__name__)
        self.angle_pairs = [f"{a:.1f},0" for a in self.angles]
        self.sun_col = 3  # sun direction column in txt output file
        

# class Longitudinal(Trace):
#     def __init__(self, min_angle, max_angle, step, rays):
#         super().__init__(min_angle, max_angle, step, rays, name=self.__class__.__name__)
#         self.angle_pairs = [f"90,{a:.1f}" for a in self.angles]
#         self.sun_col = 4  # sun direction column in txt output file
