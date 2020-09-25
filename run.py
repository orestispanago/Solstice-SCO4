from traces import Transversal, Longitudinal

transversal = Transversal(45, 135, 1, 10000)
transversal.run()
transversal.export_obj()
transversal.export_vtk()
transversal.export_heat()

longitudinal = Longitudinal(0, 25, 0.5, 10000)
longitudinal.run()
longitudinal.export_obj()
longitudinal.export_vtk()
longitudinal.export_heat()