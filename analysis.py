import os
import matplotlib.pyplot as plt
import seaborn as sns
from run import ideal_transversal_traces
from run import ideal_longitudinal_traces
import reader
import utils

sns.set_theme()

def plot_quantities(df_list, quantity="efficiency"):
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
    pic_path = os.path.join(trace.exp_dir, "plots", trace.name + "-heatmap.png")
    utils.mkdir_if_not_exists(os.path.dirname(pic_path))
    df1 = df.pivot(index='abs_y', columns='abs_x', values=values)
    sns.heatmap(df1, cbar_kws={'label': 'efficiency'},
                xticklabels=10, yticklabels=10)
    plt.title(trace.title)
    plt.savefig(pic_path)
    plt.show()


ideal_tr_df_list = [reader.read(tr) for tr in ideal_transversal_traces]
ideal_ln_df_list = [reader.read(ln) for ln in ideal_longitudinal_traces]

plot_quantities(ideal_tr_df_list)
plot_quantities(ideal_ln_df_list)

# for tr in ideal_transversal_traces:
#     plot_heatmap(tr)

# for ln in ideal_longitudinal_traces:
#     plot_heatmap(ln)
