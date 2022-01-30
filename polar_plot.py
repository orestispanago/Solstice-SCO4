import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_theme()
params = {
    "figure.figsize": (14, 4),
    "axes.titlesize": 20,
    "axes.titleweight": "bold",
    "axes.labelsize": 20,
    "axes.labelweight": "bold",
    "xtick.labelsize": 20,
    "ytick.labelsize": 20,
    "font.weight": "bold",
    "font.size": 20,
    "legend.fontsize": 16,
    "savefig.format": "png",
    # 'savefig.dpi': 300.0,
    # 'figure.constrained_layout.use': True,
}
plt.rcParams.update(params)


df = pd.read_csv(
    "export/annual-tilt38/raw/Annualall.csv", parse_dates=True, index_col="time"
)
quantity = "absorbed_flux"
# df = df.loc[(df["az"]>90) & (df["az"]<270)]
df = df.loc[(df["zenith"] < 90)]

df[["azimuth", "zenith"]].plot.hist(alpha=0.5, bins=30)


df[["azimuth", "zenith"]] = df[["azimuth", "zenith"]].apply(np.radians)


rbins = np.linspace(0, df["zenith"].max(), 30)
abins = np.linspace(0, 2 * np.pi, 60)

# The weighted histogram is the sum of all the weights for each given bin
# Divide the two, to get the average
# see https://stackoverflow.com/questions/63758336/how-to-create-a-polar-plot-with-azimuth-zenith-and-a-averaged-weight-value
hist, _, _ = np.histogram2d(df["azimuth"], df["zenith"], bins=(abins, rbins))
hist_weights, _, _ = np.histogram2d(
    df["azimuth"], df["zenith"], bins=(abins, rbins), weights=df[quantity]
)
hist_weights_kwh, _, _ = np.histogram2d(
    df["azimuth"],
    df["zenith"],
    bins=(abins, rbins),
    weights=df[quantity] / 60000,
)
# hist, _, _ = np.histogram2d(df["az"], df["zen"], density=True, weights=df["GHI"], bins=(abins, rbins))
avg_hist = hist_weights / hist
A, R = np.meshgrid(abins, rbins)


def plot_polar_heatmap(histogram, cbar_label="", pic_path=None):
    histogram[histogram == 0] = np.nan  # or use np.nan
    fig, ax = plt.subplots(subplot_kw=dict(projection="polar"), figsize=(9, 7))
    pc = ax.pcolormesh(A, R, histogram.T, cmap="jet")
    ax.set_yticklabels([])
    ax.set_theta_zero_location("N")
    fig.colorbar(pc, pad=0.1, label=cbar_label)
    ax.tick_params(pad=20)
    plt.grid()
    if pic_path:
        plt.savefig(pic_path)
    plt.show()


folder = f"export/annual-tilt38/plots/{quantity}"
plot_polar_heatmap(hist, cbar_label="count", pic_path=f"{folder}/count")
plot_polar_heatmap(
    hist_weights_kwh, cbar_label="$kWh$", pic_path=f"{folder}/kwh"
)
plot_polar_heatmap(avg_hist, cbar_label="$W$", pic_path=f"{folder}/avg_w")
