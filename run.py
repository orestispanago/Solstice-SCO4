from traces import Transversal, Longitudinal
from config import trace

tr_args = trace.transversal.values()
ln_args = trace.longitudinal.values()


transversal_plain_ideal = Transversal(*tr_args, "plain-ideal.yaml")
transversal_glass_ideal = Transversal(*tr_args, "glass-ideal.yaml")
transversal_glass_05 = Transversal(*tr_args, "glass-05.yaml")
transversal_mirrorbox = Transversal(*tr_args, "glass-ideal-mirrorbox.yaml")
transversal_mirrorbox_support = Transversal(*tr_args, "glass-ideal-mirrorbox-support.yaml")


longitudinal_plain_ideal = Longitudinal(*ln_args, "plain-ideal.yaml")
longitudinal_glass_ideal = Longitudinal(*ln_args, "glass-ideal.yaml")
longitudinal_glass_05 = Longitudinal(*ln_args, "glass-05.yaml")
longitudinal_mirrorbox = Longitudinal(*ln_args, "glass-ideal-mirrorbox.yaml")
longitudinal_mirrorbox_support = Longitudinal(*ln_args, "glass-ideal-mirrorbox-support.yaml")



if __name__ == "__main__":
    
    transversal_glass_ideal.run()
    # transversal_glass_ideal.export_obj()
    # transversal_glass_ideal.export_vtk()
    # # transversal_glass_ideal.export_heat()
    
    transversal_plain_ideal.run()
    # transversal_plain_ideal.export_obj()
    # transversal_plain_ideal.export_vtk()
    # # transversal_plain_ideal.export_heat()
    
    # longitudinal_plain_ideal.run()
    # longitudinal_glass_ideal.run()
    
    transversal_mirrorbox.run()
    # transversal_mirrorbox_support.export_obj()
    # transversal_mirrorbox.export_vtk()
    transversal_mirrorbox_support.run()
    # transversal_mirrorbox_support.export_obj()
    # transversal_mirrorbox_support.export_vtk()
    
    longitudinal_mirrorbox.run()
    longitudinal_mirrorbox_support.run()
