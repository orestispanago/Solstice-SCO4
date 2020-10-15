import matplotlib.pyplot as plt
from run import transversal_plain_ideal, transversal_glass_ideal
from run import longitudinal_plain_ideal, longitudinal_glass_ideal
import reader



def plot_quantities(df_list, quantity="efficiency"):
    fig, ax = plt.subplots()
    for df in df_list:
        ax.plot(df[quantity], label=df.label)
        ax.set_title(df.title)
        ax.set_xlabel(df.xlabel)
        ax.set_ylabel(quantity.capitalize())
    ax.legend()
    fig.savefig(f"comparison-plots/{df.title}.png")


tr_pi = reader.read(transversal_plain_ideal)
tr_gi = reader.read(transversal_glass_ideal)
ln_pi = reader.read(longitudinal_plain_ideal)
ln_gi = reader.read(longitudinal_glass_ideal)


plot_quantities([tr_pi, tr_gi])
plot_quantities([ln_pi, ln_gi])