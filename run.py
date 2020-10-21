from traces import Transversal, Longitudinal

transversal_plain_ideal = Transversal(45, 135, 1, 10000, "plain-ideal.yaml")
transversal_glass_ideal = Transversal(45, 135, 1, 10000, "glass-ideal.yaml")
transversal_glass_05 = Transversal(45, 135, 1, 10000, "glass-05.yaml")
transversal_mirrorbox = Transversal(45, 135, 1, 10000, "glass-ideal-mirrorbox.yaml")
transversal_mirrorbox_support = Transversal(45, 135, 1, 10000, "glass-ideal-mirrorbox-support.yaml")


longitudinal_plain_ideal = Longitudinal(0, 25, 0.5, 10000, "plain-ideal.yaml")
longitudinal_glass_ideal = Longitudinal(0, 25, 0.5, 10000, "glass-ideal.yaml")
longitudinal_glass_05 = Longitudinal(0, 25, 0.5, 10000, "glass-05.yaml")
longitudinal_mirrorbox = Longitudinal(0, 25, 0.5, 10000, "glass-ideal-mirrorbox.yaml")
longitudinal_mirrorbox_support = Longitudinal(0, 25, 0.5, 10000, "glass-ideal-mirrorbox-support.yaml")



if __name__ == "__main__":
    
    # transversal_glass_ideal.run_set_df()
    # transversal_glass_ideal.export_obj()
    # transversal_glass_ideal.export_vtk()
    # # transversal_glass_ideal.export_heat()
    
    # transversal_plain_ideal.run_set_df()
    # transversal_plain_ideal.export_obj()
    # transversal_plain_ideal.export_vtk()
    # # transversal_plain_ideal.export_heat()
    
    # longitudinal_plain_ideal.run()
    # longitudinal_glass_ideal.run()
    
    # transversal_mirrorbox.run()
    transversal_mirrorbox_support.export_obj()
    # transversal_mirrorbox.export_vtk()
    # transversal_mirrorbox_support.run()
    # transversal_mirrorbox_support.export_obj()
    # transversal_mirrorbox_support.export_vtk()
    
    # longitudinal_mirrorbox.run()
    # longitudinal_mirrorbox_support.run()
