import os
from directions import Transversal, Longitudinal
import config


class GeometryGroup():
    def __init__(self, group_name):
        self.group_name = group_name
        self.geometries = self.list_geometries()
        self.transversal = self.init_transversal()
        self.longitudinal = self.init_longitudinal()

    def list_geometries(self):
        geometries = [g for g in os.listdir("geometries") if g.startswith(self.group_name)]
        geometries.sort(reverse=True)
        return geometries

    def init_transversal(self):
        tr_args = config.trace.transversal.values()
        return [Transversal(*tr_args, self.group_name, g) for g in self.geometries]

    def init_longitudinal(self):
        ln_args = config.trace.longitudinal.values()
        return [Longitudinal(*ln_args, self.group_name, g) for g in self.geometries]


ideal = GeometryGroup("ideal")
errors = GeometryGroup("errors")
virtual = GeometryGroup("virtual")
