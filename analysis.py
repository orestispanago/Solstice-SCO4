import matplotlib.pyplot as plt
from run import transversal_plain_ideal, transversal_glass_ideal,transversal_mirrorbox, transversal_mirrorbox_support
from run import longitudinal_plain_ideal, longitudinal_glass_ideal, longitudinal_mirrorbox, longitudinal_mirrorbox_support
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
tr_mb = reader.read(transversal_mirrorbox)
tr_mb_sup = reader.read(transversal_mirrorbox_support)
ln_mb = reader.read(longitudinal_mirrorbox)
ln_mb_sup = reader.read(longitudinal_mirrorbox_support)

plot_quantities([tr_pi, tr_gi, tr_mb, tr_mb_sup])
plot_quantities([ln_pi, ln_gi, ln_mb, ln_mb_sup])