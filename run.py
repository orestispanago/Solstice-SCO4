import os
from traces import Transversal, Longitudinal
from config import trace


def list_geometries(geometry_type):
    geometries = [g for g in os.listdir("geometries") if g.startswith(geometry_type)]
    geometries.sort(reverse=True)
    return geometries

def init_traces(geometries):
    """ Initializes trace objects from list of geometries """
    tr_args = trace.transversal.values()
    ln_args = trace.longitudinal.values()
    transversal = [Transversal(*tr_args, g) for g in geometries]
    longitudinal = [Longitudinal(*ln_args, g) for g in geometries]
    return [transversal, longitudinal]

def traces_from_geometries(geometry_type):
    geometries = list_geometries(geometry_type)
    return init_traces(geometries)

def run_vtk_obj_heat(trace):
    trace.run()
    # trace.export_vtk()
    # trace.export_obj()
    # trace.export_heat()


ideal_transversal, ideal_longitudinal = traces_from_geometries("ideal")
errors_transversal, errors_longitudinal = traces_from_geometries("errors")
virtual_transversal, virtual_longitudinal = traces_from_geometries("virtual")


if __name__ == "__main__":

    for i in virtual_transversal:
        run_vtk_obj_heat(i)
    # for i in errors_longitudinal_traces:
    #     run_vtk_obj_heat(i)
