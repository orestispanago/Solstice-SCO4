from groups import ideal, errors, virtual
import os

print(os.environ["LD_LIBRARY_PATH"])
print(os.environ["MANPATH"])
print(os.environ["PATH"])


def run_vtk_obj_heat(trace):
    trace.run()
    # trace.export_vtk()
    # trace.export_obj()
    # trace.export_heat()


for i in errors.transversal:
    run_vtk_obj_heat(i)
for i in errors.longitudinal:
    run_vtk_obj_heat(i)
