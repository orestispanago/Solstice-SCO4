from traces import Transversal, Longitudinal

transversal = Transversal(45, 135, 1, 10000)
longitudinal = Longitudinal(0, 25, 0.5, 10000)

if __name__ == "__main__":
    
    transversal.run()
    transversal.export_obj()
    transversal.export_vtk()
    transversal.export_heat()
    
    longitudinal.run()
    longitudinal.export_obj()
    longitudinal.export_vtk()
    longitudinal.export_heat()
