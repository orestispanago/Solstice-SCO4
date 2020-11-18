import os
import matplotlib.pyplot as plt
import seaborn as sns
import utils
import reader

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
          'savefig.format': 'png',
          # 'savefig.dpi': 300.0,
          'figure.constrained_layout.use': True}
plt.rcParams.update(params)


def get_label(string):
    if string.isupper():
        return string
    return string.title().replace("_"," ")

def contains_flux_or_losses(main_str_list, substr_list=["flux", "losses"]):
    for m in main_str_list:
        for s in substr_list:
            if s in m:
                return True
    return False

def geometries_comparison(df_list, quantity="efficiency"):
    """ Plots a column of each dataframe """
    ylabel = get_label(quantity)
    fig, ax = plt.subplots(figsize=(9,6))
    for df in df_list:
        ax.plot(df[quantity], label=df.trace_geometry)
        ax.set_xlabel("$\\theta_z \quad  (\degree)$")
        ax.set_ylabel(get_label(quantity))
        if contains_flux_or_losses([quantity]):
            ylabel = ylabel + " (W)"
        ax.set_ylabel(ylabel)
    ax.legend()
    fig.savefig(f"comparison-plots/{df.trace_direction}-{quantity}")
    plt.show()

# TODO replace trace with df to remove reader
def heatmap(trace, values='efficiency'):
    df = reader.read_mean(trace)
    pic_path = os.path.join(trace.exp_dir, "heatmaps", trace.name)
    utils.mkdir_if_not_exists(os.path.dirname(pic_path))
    df1 = df.pivot(index='abs_y', columns='abs_x', values=values)
    fig, ax = plt.subplots(figsize=(10,7))  
    sns.heatmap(df1, cbar_kws={'label': 'efficiency'},
                xticklabels=10, yticklabels=10)
    plt.title(trace.title)
    plt.savefig(pic_path)
    plt.show()


def geometry_quantities(df, quantities_list):
    """ Plots list of df columns in same plot """
    pic_path = os.path.join(os.getcwd(), "export", df.trace_geometry, "plots", 
                        df.trace_direction,'-'.join(quantities_list))
    utils.mkdir_if_not_exists(os.path.dirname(pic_path))
    fig, ax = plt.subplots(figsize=(9,6))
    for col in quantities_list:        
        ax.plot(df[col], label=get_label(col))
    ax.set_xlabel("$\\theta_z \quad  (\degree)$")
    if contains_flux_or_losses(quantities_list):
        ax.set_ylabel("Watts")
    ax.legend()
    plt.savefig(pic_path)
    plt.show()
    
    
def all_quantities(df):
    for i in df.columns:
        geometry_quantities(df, [i])