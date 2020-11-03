import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from run import ideal_transversal_traces
from run import ideal_longitudinal_traces
import reader
import utils

sns.set_theme()

params = {'figure.figsize': (14, 4),
          'axes.titlesize': 20,
          'axes.titleweight': 'bold',
          'axes.labelsize': 20,
          'axes.labelweight': 'bold',
          'xtick.labelsize': 20,
          'ytick.labelsize': 20,
          'font.weight' : 'bold',
          'font.size': 20,
          'legend.fontsize': 16,
          # 'savefig.dpi': 300.0,
          # 'savefig.format': 'tiff',
          'figure.constrained_layout.use': True}
plt.rcParams.update(params)

def plot_quantity_dfs(df_list, quantity="efficiency"):
    """ Plots a column of each dataframe """
    fig, ax = plt.subplots(figsize=(9,6))
    for df in df_list:
        ax.plot(df[quantity], label=df.label)
        ax.set_xlabel("$\\theta_z \quad  (\degree)$")
        ax.set_ylabel(quantity.replace("_"," ").capitalize())
        ylabel = quantity.replace("_"," ").capitalize()
        if contains_flux_or_losses([quantity]):
            ylabel = ylabel + " (W)"
        ax.set_ylabel(ylabel)
    ax.legend()
    fig.savefig(f"comparison-plots/{df.title}-{quantity}.png")
    plt.show()


def plot_heatmap(trace, values='efficiency'):
    df = reader.read_mean(trace)
    pic_path = os.path.join(trace.exp_dir, "heatmaps", trace.name + ".png")
    utils.mkdir_if_not_exists(os.path.dirname(pic_path))
    df1 = df.pivot(index='abs_y', columns='abs_x', values=values)
    fig, ax = plt.subplots(figsize=(10,7))  
    sns.heatmap(df1, cbar_kws={'label': 'efficiency'},
                xticklabels=10, yticklabels=10)
    plt.title(trace.title)
    plt.savefig(pic_path)
    plt.show()

def contains_flux_or_losses(main_str_list, substr_list=["flux", "losses"]):
    for m in main_str_list:
        for s in substr_list:
            if s in m:
                return True
    return False


ideal_tr_df_list = [reader.read(tr) for tr in ideal_transversal_traces]
ideal_ln_df_list = [reader.read(ln) for ln in ideal_longitudinal_traces]

plot_quantity_dfs(ideal_tr_df_list[-2:])
plot_quantity_dfs(ideal_ln_df_list[-2:])

# for tr in ideal_transversal_traces:
#     plot_heatmap(tr)

# for ln in ideal_longitudinal_traces:
#     plot_heatmap(ln)

df = ideal_tr_df_list[-1]

# TODO check calculation with partners
df["intercept_factor"] = df["absorbed_flux"]/ (df["potential_flux"] * df["cos_factor"])
# Used to confirm absorbed calculation
# df["calculated_absorbed"] = df["potential_flux"]*df["cos_factor"] - \
#                                 df["shadow_losses"] - \
#                                 df["missing_losses"] -\
#                                 df["reflectivity_losses"] - \
#                                 df["absorptivity_losses"]

def plot_columns_list(df, columns_list):
    """ Plots list of columns in same plot """
    pic_path = os.path.join(os.getcwd(), "export", "ideal-frame-mirrorbox-support", "plots", 
                            df.title,'-'.join(columns_list)+".png")
    utils.mkdir_if_not_exists(os.path.dirname(pic_path))
    fig, ax = plt.subplots(figsize=(9,6))
    for col in columns_list:        
        ax.plot(df[col], label=col.title().replace("_"," "))
    ax.set_xlabel("$\\theta_z \quad  (\degree)$")
    if contains_flux_or_losses(columns_list):
        ax.set_ylabel("Watts")
    ax.legend()
    plt.savefig(pic_path)
    plt.show()
    
# plot_columns_list(df, ["intercept_factor", "efficiency"])


# for i in df.columns:
#     plot_columns_list(df, [i])
