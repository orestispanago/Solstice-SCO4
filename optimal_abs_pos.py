import pandas as pd
import numpy as np
from tqdm import tqdm
from mirror_coordinates import centered_x, centered_y
from mod_geometry import move_absorber
from run import ideal_transversal_traces
from run import ideal_longitudinal_traces
import reader
from config import trace


def change_abs_run_mean(trace, step=trace.absorber_shift_step):
    """ Changes absorber position, 
    runs trace with output to dataframe (as Trace class attribute),
    calculates mean of dataframe column
    returns new dataframe with coords and column mean """
    df = pd.DataFrame(columns=["abs_x", "abs_y", "efficiency",
                               "potential_flux", "absorbed_flux",
                               "cos_factor", "shadow_losses"])
    for x in tqdm(np.arange(round(centered_x[0], 1), round(centered_x[-1], 1) + 0.0001, step)):
        for y in np.arange(round(centered_y[0], 1), round(centered_y[-1], 1) + 0.0001, step):
            move_absorber(trace.geometry, x, y)
            trace.run_set_df()
            tr_df = reader.read(trace)
            df = df.append({"abs_x": round(x, 3),
                            "abs_y": round(y, 3),
                            "efficiency": tr_df["efficiency"].mean(),
                            "potential_flux": tr_df["potential_flux"].mean(),
                            "absorbed_flux": tr_df["absorbed_flux"].mean(),
                            "cos_factor": tr_df["cos_factor"].mean(),
                            "shadow_losses": tr_df["shadow_losses"].mean()
                            }, ignore_index=True)
    move_absorber(trace.geometry, 0, 0)
    df.to_csv(trace.meanfile, index=False)

# change_abs_run_mean(transversal_mirrorbox_support)
# change_abs_run_mean(longitudinal_mirrorbox_support)
