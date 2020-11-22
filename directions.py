import os
import numpy as np

CWD = os.getcwd()


class Direction:

    def __init__(self, min_angle, max_angle, step, rays, geometry_group, geometry):
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.step = step
        self.rays = rays
        self.geometry_group = geometry_group
        self.geometry = geometry
        self.geometry_name = geometry.split(".")[0]
        self.angles = np.arange(min_angle, max_angle + 1, step).tolist()
        self.receiver = os.path.join(CWD, "geometries", "receiver.yaml")
        self.geometry_path = os.path.join(CWD, "geometries", self.geometry)
        self.shape_dir = os.path.join(CWD, 'export', self.geometry_name,
                                      "shapes")
        self.raw_file = os.path.join(CWD, 'export', self.geometry_name, 'raw',
                                     self.__class__.__name__ + ".txt")


class Transversal(Direction):
    def __init__(self, min_angle, max_angle, step, rays, geometry_group, geometry):
        super().__init__(min_angle, max_angle, step, rays, geometry_group, geometry)
        self.angle_pairs = [f"{a:.1f},0" for a in self.angles]
        self.sun_col = 3  # sun direction column in txt output file


class Longitudinal(Direction):
    def __init__(self, min_angle, max_angle, step, rays, geometry_group, geometry):
        super().__init__(min_angle, max_angle, step, rays, geometry_group, geometry)
        self.angle_pairs = [f"90,{a:.1f}" for a in self.angles]
        self.sun_col = 4  # sun direction column in txt output file
