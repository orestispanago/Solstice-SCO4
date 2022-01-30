from groups import ideal, errors, virtual
import reader
import plots


def calc_shadow_losses(df, virtual_df):
    df["mirrors_shadow_losses"] = virtual_df["shadow_losses"]
    df["receiver_shadow_losses"] = df["shadow_losses"] - df["mirrors_shadow_losses"]


ideal_tr_dfs = reader.read_list(ideal.transversal)
ideal_ln_dfs = reader.read_list(ideal.longitudinal)

errors_tr_dfs = reader.read_list(errors.transversal)
errors_ln_dfs = reader.read_list(errors.longitudinal)

virtual_mirror_plane = reader.read(virtual.transversal[0])
virtual_abs_tr = reader.read(virtual.transversal[1])
virtual_abs_ln = reader.read(virtual.longitudinal[1])

virtual_abs_10x6_tr = reader.read(virtual.transversal[2])
virtual_abs_10x6_ln = reader.read(virtual.longitudinal[2])

ideal_plain_tr = ideal_tr_dfs[0]
ideal_plain_ln = ideal_ln_dfs[0]

ideal_plain_10x6_tr = ideal_tr_dfs[1]
ideal_plain_10x6_ln = ideal_ln_dfs[1]

calc_shadow_losses(ideal_plain_tr, virtual_abs_tr)
calc_shadow_losses(ideal_plain_10x6_tr, virtual_abs_10x6_tr)

virtual_mirr_plane_tr = reader.read(virtual.transversal[0])
# plots.geometry_quantities(virtual_mirr_plane_tr, ["absorbed_flux", "shadow_losses"])


ideal_plain_tr["gamma"] = ideal_plain_tr["absorbed_flux"]/\
    (virtual_mirr_plane_tr['potential_flux'] - \
      virtual_mirr_plane_tr["shadow_losses"])
     
ideal_plain_tr["IAM"] = ideal_plain_tr["gamma"] / ideal_plain_tr["gamma"][0]
plots.geometry_quantities(
    ideal_plain_tr,
    ["efficiency", "gamma", "intercept_factor", "IAM"],
)
# plots.geometry_quantities(
#     ideal_plain_tr,
#     ["shadow_losses", "mirrors_shadow_losses", "receiver_shadow_losses"],
# )
# plots.geometry_quantities(ideal_plain_tr, ["intercept_factor"])
# plots.geometry_quantities(ideal_plain_ln, ["intercept_factor"])

# plots.geometries_comparison([ideal_tr_dfs[0], ideal_tr_dfs[1]], "efficiency")
# plots.geometries_comparison([ideal_tr_dfs[0], ideal_tr_dfs[1]], "potential_flux")
# plots.geometries_comparison([ideal_tr_dfs[0], ideal_tr_dfs[1]], "absorbed_flux")

# plots.all_quantities(ideal_plain_ln)
# plots.all_quantities(ideal_plain_tr)
# plots.geometries_comparison([ideal_plain, virtual_abs], quantity="shadow_losses")
# plots.geometries_comparison(ideal_tr_dfs[:2], quantity="IAM")

# plots.geometries_comparison([errors_tr_dfs[0],ideal_tr_dfs[0]], quantity="IAM")
# plots.geometries_comparison([errors_ln_dfs[1],ideal_ln_dfs[0]], quantity="IAM")
# ideal_plain_mean = reader.read_aggregate(ideal.transversal[0], "mean")
# plots.heatmap(ideal_plain_mean)

# for ln in ideal_longitudinal_traces:
#     plot_heatmap(ln)
