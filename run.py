from traces import Transversal, Longitudinal

transversal_plain_ideal = Transversal(45, 135, 1, 10000, "plain-ideal.yaml")
transversal_glass_ideal = Transversal(45, 135, 1, 10000, "glass-ideal.yaml")
transversal_glass_05 = Transversal(45, 135, 1, 10000, "glass-05.yaml")


longitudinal_plain_ideal = Longitudinal(0, 25, 0.5, 10000, "plain-ideal.yaml")
longitudinal_glass_ideal = Longitudinal(0, 25, 0.5, 10000, "glass-ideal.yaml")
longitudinal_glass_05 = Longitudinal(0, 25, 0.5, 10000, "glass-05.yaml")


# transversal_plain_ideal.run_to_df()
# transversal_glass_ideal.run_to_df()
# transversal_glass_05.run_to_df()


if __name__ == "__main__":
    
    # transversal_glass_05.run()
    # transversal_glass_05.export_obj()
    # transversal_glass_05.export_vtk()
    # # transversal.export_heat()
    
    # longitudinal_glass_05.run()
    # longitudinal_glass_05.export_obj()
    # longitudinal_glass_05.export_vtk()
    # longitudinal.export_heat()
    
    # transversal_glass_ideal.run()
    # transversal_glass_ideal.export_obj()
    # transversal_glass_ideal.export_vtk()
    
    # longitudinal_glass_ideal.run()
    # longitudinal_glass_ideal.export_obj()
    # longitudinal_glass_ideal.export_vtk()
    
    transversal_plain_ideal.run_to_df()
    transversal_glass_ideal.run_to_df()
    transversal_glass_05.run_to_df()