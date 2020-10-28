import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from run import ideal_transversal_traces
from run import ideal_longitudinal_traces
import reader
import utils

sns.set_theme()

def plot_quantity_dfs(df_list, quantity="efficiency"):
    """ Plots a column of each dataframe """
    fig, ax = plt.subplots(figsize=(9,6))
    for df in df_list:
        ax.plot(df[quantity], label=df.label)
        ax.set_title(df.title)
        ax.set_xlabel(df.xlabel)
        ax.set_ylabel(quantity.capitalize())
    ax.legend()
    # plt.grid()
    fig.savefig(f"comparison-plots/{df.title}-{quantity}.png")
    plt.show()


def plot_heatmap(trace, values='efficiency'):
    df = reader.read_mean(trace)
    pic_path = os.path.join(trace.exp_dir, "heatmaps", trace.name + ".png")
    utils.mkdir_if_not_exists(os.path.dirname(pic_path))
    df1 = df.pivot(index='abs_y', columns='abs_x', values=values)
    sns.heatmap(df1, cbar_kws={'label': 'efficiency'},
                xticklabels=10, yticklabels=10)
    plt.title(trace.title)
    plt.savefig(pic_path)
    plt.show()


ideal_tr_df_list = [reader.read(tr) for tr in ideal_transversal_traces]
ideal_ln_df_list = [reader.read(ln) for ln in ideal_longitudinal_traces]

# plot_quantity_dfs(ideal_tr_df_list)
# plot_quantity_dfs(ideal_ln_df_list)

# for tr in ideal_transversal_traces:
#     plot_heatmap(tr)

# for ln in ideal_longitudinal_traces:
#     plot_heatmap(ln)

df = ideal_tr_df_list[0]
df.index = df.index-90
df["cos_index"] = np.cos(np.deg2rad(df.index))
df["intercept_factor"] = df["efficiency"]/df["cos_index"]
df["total"] = df["potential_flux"]*df["cos_factor"] - \
                                df["shadow_losses"] - \
                                df["missing_losses"] -\
                                df["reflectivity_losses"] - \
                                df["absorptivity_losses"]

def plot_columns_list(df, columns_list):
    """ Plots list of columns in same plot """
    pic_path = os.path.join(os.getcwd(), "export", "ideal-plain", "plots", 
                            "Transversal",'-'.join(columns_list)+".png")
    utils.mkdir_if_not_exists(os.path.dirname(pic_path))
    fig, ax = plt.subplots(figsize=(9,6))
    for col in columns_list:        
        ax.plot(df[col], label=col.title().replace("_"," "))
    ax.legend()
    plt.savefig(pic_path)
    plt.show()
    
plot_columns_list(df, ["intercept_factor", "efficiency"])
# plot_quantities(df, "cos_factor", "cos_90_index")
# plot_quantities(df, "absorbed_flux", "total")


for i in df.columns:
    plot_columns_list(df, [i])
    