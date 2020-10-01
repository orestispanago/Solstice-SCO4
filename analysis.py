import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from run import transversal_plain_ideal, transversal_glass_ideal, transversal_glass_05


columns = {"potential_flux": 2,
           "absorbed_flux": 3,
           "cos_factor": 4,
           "shadow_losses": 5
           }

def read(trace):
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
    for i in columns:
        plt.plot(df[i])
        plt.title(df.name)
        plt.ylabel(i.replace("_"," ").title())
        plt.xticks(np.arange(30,145,10))
        plt.xlim(40, 140)
        plt.show()

def plot_effs(df_list):
    for df in df_list:
        plt.plot(df["efficiency"])
    plt.show()
    
    
tr_pi = read(transversal_plain_ideal)
tr_gi = read(transversal_glass_ideal)
tr_g05 = read(transversal_glass_05)
# plot_cols(tr_pi)    
plot_effs([tr_pi, tr_gi, tr_g05])
