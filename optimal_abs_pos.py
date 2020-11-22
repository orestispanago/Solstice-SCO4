import os
import pandas as pd
import numpy as np
from tqdm import tqdm
import export
from mirror_coordinates import centered_x, centered_y
from mod_geometry import move_absorber
from groups import ideal
import reader
import config


def abs_positions(coords):
    # step = config.direction.absorber_shift_step
    step = 0.2
    return np.arange(round(coords[0], 1), round(coords[-1], 1) + 0.0001, step)


def move_abs_run_agg(direction, aggregate):
    """ Changes absorber position, 
    runs direction with output to dataframe (as Direction class attribute),
    calculates aggregate of dataframe columns (sum, mean, etc)
    returns new dataframe with coords and columns aggregate """
    cols = ["efficiency", *reader.columns.keys()]
    df = pd.DataFrame(columns=["abs_x", "abs_y", *cols])
    for x in tqdm(abs_positions(centered_x)):
        for y in abs_positions(centered_y):
            move_absorber(direction.geometry_path, x, y)
            direction.df = export.df(direction)
            tr_df = reader.read(direction)
            df = df.append(
                {"abs_x": round(x, 3),
                 "abs_y": round(y, 3),
                 "efficiency": getattr(tr_df["efficiency"], aggregate)(),
                 "potential_flux": getattr(tr_df["potential_flux"], aggregate)(),
                 "absorbed_flux": getattr(tr_df["absorbed_flux"], aggregate)(),
                 "cos_factor": getattr(tr_df["cos_factor"], aggregate)(),
                 "shadow_losses": getattr(tr_df["shadow_losses"], aggregate)()
                 }, ignore_index=True)
    move_absorber(direction.geometry_path, 0, 0)
    csvpath = os.path.join(os.getcwd(), 'export', direction.geometry_name, 'raw',
                           f"{direction.__class__.__name__}-{aggregate}.csv")
    df.to_csv(csvpath, index=False)


transversal_mirrorbox_support = ideal.transversal[-2]
longitudinal_mirrorbox_support = ideal.longitudinal[-2]

# move_abs_run_mean(transversal_mirrorbox_support, "sum")
# move_abs_run_mean(longitudinal_mirrorbox_support, "sum")
for i in [ideal.transversal[0],
          ideal.transversal[-2],
          ideal.longitudinal[0],
          ideal.longitudinal[-2]]:
    move_abs_run_agg(i, "sum")
