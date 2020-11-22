from groups import ideal, errors, virtual
from setup import check_installation

check_installation()


def run_vtk_obj_heat(trace):
    trace.run()
    # trace.export_vtk()
    # trace.export_obj()
    # trace.export_heat()


for i in errors.transversal:
    run_vtk_obj_heat(i)
for i in errors.longitudinal:
    run_vtk_obj_heat(i)
