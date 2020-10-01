from traces import Transversal

# transversal = Transversal(45, 135, 1, 10000)
# longitudinal = Longitudinal(0, 25, 0.5, 10000)
transversal_plain_ideal = Transversal(45, 135, 1, 10000, "plain-ideal.yaml")
transversal_glass_ideal = Transversal(45, 135, 1, 10000, "glass-ideal.yaml")

if __name__ == "__main__":
    
    transversal_plain_ideal.run()
    transversal_plain_ideal.export_obj()
    transversal_plain_ideal.export_vtk()
    # transversal.export_heat()
    
    # longitudinal.run()
    # longitudinal.export_obj()
    # longitudinal.export_vtk()
    # longitudinal.export_heat()
