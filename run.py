from traces import Transversal, Longitudinal

transversal_plain_ideal = Transversal(45, 135, 1, 10000, "plain-ideal.yaml")
transversal_glass_ideal = Transversal(45, 135, 1, 10000, "glass-ideal.yaml")
transversal_glass_05 = Transversal(45, 135, 1, 10000, "glass-05.yaml")


longitudinal_plain_ideal = Longitudinal(0, 25, 0.5, 10000, "plain-ideal.yaml")
longitudinal_glass_ideal = Longitudinal(0, 25, 0.5, 10000, "glass-ideal.yaml")
longitudinal_glass_05 = Longitudinal(0, 25, 0.5, 10000, "glass-05.yaml")


if __name__ == "__main__":
    
    transversal_glass_05.run()
    transversal_glass_05.export_obj()
    transversal_glass_05.export_vtk()
    # transversal.export_heat()
    
    longitudinal_glass_05.run()
    longitudinal_glass_05.export_obj()
    longitudinal_glass_05.export_vtk()
    # longitudinal.export_heat()
