import pandas as pd
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
from mirror_coordinates import centered_x, centered_y
from mod_geometry import move_absorber
from run import (transversal_plain_ideal, 
                 transversal_glass_ideal,
                 transversal_mirrorbox, 
                 transversal_mirrorbox_support)
from run import (longitudinal_plain_ideal, 
                 longitudinal_glass_ideal,
                 longitudinal_mirrorbox,
                 longitudinal_mirrorbox_support)
import reader


def change_abs_run_mean(trace, step=0.02):
    """ Changes absorber position, 
    runs trace with output to dataframe (as Trace class attribute),
    calculates mean of dataframe column
    returns new dataframe with coords and column mean """
    df = pd.DataFrame(columns=["abs_x", "abs_y", "efficiency", 
                               "potential_flux", "absorbed_flux", 
                               "cos_factor", "shadow_losses" ])
    for x in tqdm(np.arange(round(centered_x[0],1), round(centered_x[-1],1)+0.0001, step)):
        for y in np.arange(round(centered_y[0],1), round(centered_y[-1],1)+0.0001, step):
            move_absorber(trace.geometry, x, y)
            trace.run_set_df()
            tr_df = reader.read(trace)
            df = df.append({"abs_x": round(x,3), 
                            "abs_y":  round(y,3), 
                            "efficiency": tr_df["efficiency"].mean(),
                            "potential_flux": tr_df["potential_flux"].mean(),
                            "absorbed_flux": tr_df["absorbed_flux"].mean(),
                            "cos_factor": tr_df["cos_factor"].mean(),
                            "shadow_losses": tr_df["shadow_losses"].mean()
                            }, ignore_index=True)
    move_absorber(trace.geometry, 0, 0)
    df.title=trace.title
    df.to_csv(f'{trace.rawfile.split(".")[0]}-{step}-means.csv', index=False)
    return df


def plot_heatmap(df, values='efficiency'):
    tracename = df.title.split(" ")
    fpath = f'export/{tracename[1]}/plots/{tracename[0]}-heatmap.png'
    df1 = df.pivot(index='abs_y', columns='abs_x', values='efficiency')
    xticks = df1.columns
    yticks = df1.index
    xticklabels = [df1.columns[i] for i in xticks]
    yticklabels = [df1.index[i] for i in yticks]
    heatmap = sns.heatmap(df1, cbar_kws={'label': 'efficiency'}, 
                          yticklabels=yticklabels,
                          xticklabels=xticklabels)
    heatmap.set_xticks(xticks)
    heatmap.set_yticks(yticks)
    plt.title(df.title)
    plt.savefig(fpath)
    plt.show()


result = change_abs_run_mean(transversal_glass_ideal)
#plot_heatmap(result)


result1 = change_abs_run_mean(longitudinal_glass_ideal)
#plot_heatmap(result1)