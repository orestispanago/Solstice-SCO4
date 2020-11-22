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

ideal_plain_tr = ideal_tr_dfs[0]

calc_shadow_losses(ideal_plain_tr, virtual_abs_tr)
# plots.geometry_quantities(ideal_plain_tr, [
#                                         "shadow_losses", 
#                                         "mirrors_shadow_losses",
#                                         "receiver_shadow_losses"])


# plots.geometries_comparison([ideal_tr_dfs[0], errors_tr_dfs[2]], "absorbed_flux")
# plots.geometries_comparison([ideal_ln_dfs[0], errors_ln_dfs[2]], "absorbed_flux")

# plots.all_quantities(ideal_plain_tr)
# plot_geometries_comparison([ideal_plain, virtual_abs], quantity="shadow_losses")
# plot_geometries_comparison(ideal_tr_dfs[:2], quantity="IAM")

# plot_geometries_comparison([errors_tr_dfs[0],ideal_tr_dfs[0]], quantity="IAM")
# plot_geometries_comparison([errors_ln_dfs[1],ideal_ln_dfs[0]], quantity="IAM")
ideal_plain_mean = reader.read_mean(ideal.transversal[0])
plots.heatmap(ideal_plain_mean)

# for ln in ideal_longitudinal_traces:
#     plot_heatmap(ln)


# plot_geometries_comparison(ideal_tr_df_list[-2])
