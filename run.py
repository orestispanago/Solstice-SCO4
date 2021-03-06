from groups import ideal, errors, virtual
from setup import check_installation
import export


def csv_vtk_obj_heat(direction):
    export.csv(direction)
    export.vtk(direction)
    export.obj(direction)
    # export.heatmap(direction)


for i in ideal.transversal:
    csv_vtk_obj_heat(i)
for i in ideal.longitudinal:
    csv_vtk_obj_heat(i)
