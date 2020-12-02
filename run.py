from groups import ideal, errors, virtual
from setup import check_installation
import export


def raw_vtk_obj_heat(direction):
    # export.raw(direction)
    export.vtk(direction)
    export.obj(direction)
    # export.heatmap(direction)


# for i in ideal.transversal:
#     raw_vtk_obj_heat(i)
# for i in ideal.longitudinal:
#     raw_vtk_obj_heat(i)
raw_vtk_obj_heat(ideal.longitudinal[0])