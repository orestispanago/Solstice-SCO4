import numpy as np
import os
import subprocess

exp_dir = os.path.join(os.getcwd(), 'raw')
geom_dir = os.path.join(os.getcwd(), "geometry")
geometry = os.path.join(geom_dir, "geometry1.yaml")  # Path needs to be set in file
receiver = os.path.join(geom_dir, "receiver.yaml")
exp_shapes_dir = os.path.join(os.getcwd(), "export-shapes")


class Trace():

    def __init__(self, min_angle, max_angle, step, rays):
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.step = step
        self.rays = rays
        self.angles = np.arange(min_angle, max_angle + 1, step).tolist()

    def run(self):
        with open(self.outfile, 'w') as f:
            # Solstice cannot take too long string of angle arguments, so split into chunks
            for i in range(0, len(self.angle_pairs), 50):
                chunk = self.angle_pairs[i:i + 50]
                chunk = ":".join(chunk)
                cmd = f'solstice -D {chunk} -n {self.rays} -v -R {receiver} {geometry}'.split()
                subprocess.run(cmd, stdout=f)

    def export_vtk(self, nrays=100):
        for pair in [self.angle_pairs[0], self.angle_pairs[-1]]:
            pair_str = pair.replace(',', '_')
            fname = f"{self.name}_{pair_str}.vtk"
            vtkpath = os.path.join(exp_shapes_dir, fname)
            cmd = f'solstice  -n {nrays} -p default -t1 -D {pair} -R {receiver} {geometry}'.split()
            with open(vtkpath, 'w') as f:
                subprocess.run(cmd, stdout=f)
            del_first_line(vtkpath)

    def export_obj(self):
        for pair in [self.angle_pairs[0], self.angle_pairs[-1]]:
            pair_str = pair.replace(',', '_')
            fname = f"{self.name}_{pair_str}.obj"
            objpath = os.path.join(exp_shapes_dir, fname)
            cmd = f'solstice  -n 100 -g format=obj -t1 -D {pair} -R {receiver} {geometry}'.split()
            with open(objpath, 'w') as f:
                subprocess.run(cmd, stdout=f)


class Transversal(Trace):
    def __init__(self, min_angle, max_angle, step, rays):
        super().__init__(min_angle, max_angle, step, rays)
        self.name = "transversal"
        self.angle_pairs = [f"{a:.1f},0" for a in self.angles]
        self.sun_col = 3  # sun direction column in txt output file
        self.outfile = os.path.join(exp_dir, self.name + ".txt")


class Longitudinal(Trace):
    def __init__(self, min_angle, max_angle, step, rays):
        super().__init__(min_angle, max_angle, step, rays)
        self.name = "longitudinal"
        self.angle_pairs = [f"90,{a:.1f}" for a in self.angles]
        self.sun_col = 4  # sun direction column in txt output file
        self.outfile = os.path.join(exp_dir, self.name + ".txt")


def del_first_line(fname):
    # Deletes first line from vtk file to be opened by Paraview
    with open(fname, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(fname, 'w') as fout:
        fout.writelines(data[1:])
