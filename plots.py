import os

import matplotlib.pyplot as plt
import seaborn as sns

import utils

# sns.set_theme()

params = {
    "figure.figsize": (14, 4),
    "axes.titlesize": 28,
    "axes.titleweight": "bold",
    "axes.labelsize": 28,
    "axes.labelweight": "bold",
    "axes.grid" : True,
    'lines.linewidth':6.0,
    "xtick.labelsize": 28,
    "ytick.labelsize": 28,
    "font.weight": "bold",
    "font.size": 28,
    "legend.fontsize": 20,
    "savefig.format": "png",
    # 'savefig.dpi': 300.0,
    "figure.constrained_layout.use": True,
}
plt.rcParams.update(params)


def get_label(string):
    if string.isupper():
        return string
    return string.title().replace("_", " ")


def contains_flux_or_losses(main_str_list, substr_list=["flux", "losses"]):
    for m in main_str_list:
        for s in substr_list:
            if s in m:
                return True
    return False


def geometries_comparison(df_list, quantity="efficiency"):
    """Plots a column of each dataframe"""
    ylabel = get_label(quantity)
    fig, ax = plt.subplots(figsize=(9, 6))
    for df in df_list:
        ax.plot(df[quantity], label=df.direction_geometry)
    ax.set_xlabel("$\\theta_z \quad  (\degree)$")
    ax.set_ylabel(get_label(quantity))
    if contains_flux_or_losses([quantity]):
        ylabel = ylabel + " (W)"
    ax.set_ylabel(ylabel)
    ax.legend()
    fig.savefig(f"comparison-plots/{df.direction_name}-{quantity}")
    plt.show()


# TODO replace direction with df to remove reader
def heatmap(df, col="efficiency"):
    pic_path = os.path.join(
        os.getcwd(),
        "export",
        df.direction_geometry,
        "heatmaps",
        df.direction_name + col,
    )
    utils.mkdir_if_not_exists(os.path.dirname(pic_path))
    df1 = df.pivot(index="abs_y", columns="abs_x", values=col)
    fig, ax = plt.subplots(figsize=(10, 7))
    sns.heatmap(df1, cbar_kws={"label": col}, xticklabels=10, yticklabels=10)
    plt.title(df.direction_geometry)
    plt.savefig(pic_path)
    plt.show()


def geometry_quantities(df, quantities_list):
    """Plots list of df columns in same plot"""
    pic_path = os.path.join(
        os.getcwd(),
        "export",
        df.direction_geometry,
        "plots",
        df.direction_name,
        "-".join(quantities_list),
    )
    utils.mkdir_if_not_exists(os.path.dirname(pic_path))
    fig, ax = plt.subplots(figsize=(9, 6))
    for col in quantities_list:
        ax.plot(df[col], label=get_label(col))
        ax.set_title(get_label(col))
    ax.set_xlabel("Incidence angle $\\theta \ (\degree)$")
    if contains_flux_or_losses(quantities_list):
        ax.set_ylabel("Watts")
    # ax.legend()
    
    plt.savefig(pic_path)
    plt.show()


def all_quantities(df):
    for i in df.columns:
        geometry_quantities(df, [i])
