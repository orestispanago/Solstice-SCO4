import os
from traces import Transversal, Longitudinal
from config import trace

tr_args = trace.transversal.values()
ln_args = trace.longitudinal.values()

ideal_geometries = [g for g in os.listdir("geometries") if g.startswith("ideal")]
ideal_geometries.sort(reverse=True)

errors_geometries = [g for g in os.listdir("geometries") if g.startswith("errors")]
errors_geometries.sort(reverse= True)

ideal_transversal_traces = [Transversal(*tr_args, g) for g in ideal_geometries]
ideal_longitudinal_traces = [Longitudinal(*ln_args, g) for g in ideal_geometries]

errors_transversal_traces = [Transversal(*tr_args, g) for g in errors_geometries]
errors_longitudinal_traces = [Longitudinal(*ln_args, g) for g in errors_geometries]

def run_vtk_obj_heat(trace):
    trace.run()
    # trace.export_vtk()
    # trace.export_obj()
    # trace.export_heat()


if __name__ == "__main__":

    for i in errors_transversal_traces:
        run_vtk_obj_heat(i)
    for i in errors_longitudinal_traces:
        run_vtk_obj_heat(i)
