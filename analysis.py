import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
from run import transversal_plain_ideal, transversal_glass_ideal, transversal_glass_05
from run import longitudinal_plain_ideal, longitudinal_glass_ideal, longitudinal_glass_05
from mirror_coordinates import centered_x, centered_y, move_absorber

columns = {"potential_flux": 2,
           "absorbed_flux": 3,
           "cos_factor": 4,
           "shadow_losses": 5
           }

def read(trace):
    if trace.df is not None:
        df = trace.df
    else:
        df = pd.read_csv(trace.rawfile, sep='\s+',names=range(47))
    trace_df = df.loc[df[1] == 'Sun', [trace.sun_col]]  # set 4 for longitudinal
    trace_df.columns = ["angle"]
    trace_df["efficiency"] = df.loc[df[0] == 'absorber',[23]].values # Overall effficiency, add [23,24] for error
    for key in columns.keys():
        trace_df[key] = df[0].iloc[trace_df.index + columns.get(key)].astype('float').values
    trace_df = trace_df.set_index("angle")
    trace_df.name = trace.name
    return trace_df

def plot_cols(df):
    for col in df.columns:
        plt.plot(df[col])
        plt.title(df.name)
        plt.ylabel(col.replace("_"," ").title())
        if df.name == "Transversal":
            plt.xticks(np.arange(30,145,10))
            plt.xlim(40, 140)
        plt.show()

def plot_effs(df_list):
    for df in df_list:
        plt.plot(df["efficiency"])
        plt.ylabel("Overall efficiency")
    plt.show()
    
    
# tr_pi = read(transversal_plain_ideal)
# tr_gi = read(transversal_glass_ideal)
# tr_g05 = read(transversal_glass_05)
# # plot_cols(tr_pi)    
# plot_effs([tr_pi, tr_gi])


# ln_pi = read(longitudinal_plain_ideal)
# ln_gi = read(longitudinal_glass_ideal)
# ln_g05 = read(longitudinal_glass_05)
# # plot_cols(ln_pi)    
# plot_effs([ln_pi, ln_gi])


def change_abs_run_mean(trace, step=0.05):
    """ Changes absorber position, 
    runs trace with output to dataframe (as Trace class attribute),
    calculates mean of dataframe column
    returns new dataframe with coords and column mean """
    df = pd.DataFrame(columns=["abs_x", "abs_y", "efficiency", 
                               "potential_flux", "absorbed_flux", 
                               "cos_factor", "shadow_losses" ])
    for x in tqdm(np.arange(centered_x[0], centered_x[-1], step)):
        for y in np.arange(centered_y[0], centered_y[-1], step):
            move_absorber(trace.geometry, x, y)
            trace.run_to_df()
            tr_df = read(trace)
            df = df.append({"abs_x": round(x,3), 
                            "abs_y":  round(y,3), 
                            "efficiency": tr_df["efficiency"].mean(),
                            "potential_flux": tr_df["potential_flux"].mean(),
                            "absorbed_flux": tr_df["absorbed_flux"].mean(),
                            "cos_factor": tr_df["cos_factor"].mean(),
                            "shadow_losses": tr_df["shadow_losses"].mean()
                            }, ignore_index=True)
    move_absorber(trace.geometry, 0, 0)
    df.name=trace.name
    return df


def plot_heatmap(df, values='efficiency'):
    tracename = df.name.split(" ")
    fpath = f'export/{tracename[1]}/plots/{tracename[0]}-heatmap.png'
    df1 = df.pivot(index='abs_y', columns='abs_x', values=values)
    heatmap = sns.heatmap(df1, cbar_kws={'label': values})
    plt.locator_params(axis='y', nbins=8)   # y-axis
    plt.locator_params(axis='x', nbins=6)  # x-axis
    plt.title(df.name)
    plt.savefig(fpath)
    


result = change_abs_run_mean(transversal_plain_ideal)
plot_heatmap(result)