from groups import ideal, errors, virtual
from setup import check_installation
import export


def raw_vtk_obj_heat(trace):
    export.raw(trace)
    # export.vtk(trace)
    # export.obj(trace)
    # export.heat(trace)


for i in errors.transversal:
    raw_vtk_obj_heat(i)
for i in errors.longitudinal:
    raw_vtk_obj_heat(i)
