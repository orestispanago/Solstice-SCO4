from groups import ideal, errors, virtual


def run_vtk_obj_heat(trace):
    trace.run()
    # trace.export_vtk()
    # trace.export_obj()
    # trace.export_heat()


for i in virtual.transversal:
    run_vtk_obj_heat(i)
# for i in errors_longitudinal_traces:
#     run_vtk_obj_heat(i)
