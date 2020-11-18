from groups import ideal, errors, virtual
import reader
import plots


ideal_tr_dfs = reader.read_list(ideal.transversal)
ideal_ln_dfs = reader.read_list(ideal.longitudinal)

errors_tr_dfs = reader.read_list(errors.transversal)
errors_ln_dfs = reader.read_list(errors.longitudinal)

virtual_mirror_plane = reader.read(virtual.transversal[0])
virtual_abs = reader.read(virtual.transversal[1])

ideal_plain = ideal_tr_dfs[0]

ideal_plain["mirrors_shadow_losses"] = virtual_abs["shadow_losses"]
ideal_plain["receiver_shadow_losses"] = ideal_plain["shadow_losses"] - ideal_plain["mirrors_shadow_losses"]

# plot_geometry_quantities(ideal_plain, [
#                                         "shadow_losses", 
#                                        "mirrors_shadow_losses",
#                                        "receiver_shadow_losses"])

virtual_abs["FpCf"] = virtual_abs["potential_flux"] * virtual_abs["cos_factor"]
virtual_abs["incident"] = virtual_abs["FpCf"] - virtual_abs["shadow_losses"]
# plot_geometry_quantities(virtual_abs, ["FpCp", "incident"])
# TODO check intercept factor denominator in reader

virtual_mirror_plane["FpCf"] = virtual_mirror_plane["potential_flux"] * virtual_mirror_plane["cos_factor"]
ideal_plain["FpCf"] = ideal_plain["potential_flux"] * ideal_plain["cos_factor"]

plots.geometries_comparison([ideal_plain,virtual_mirror_plane], quantity="FpCf")



ideal_plain["intercep_factorG"] = ideal_plain["absorbed_flux"] / \
    (ideal_plain["FpCf"] - ideal_plain["missing_losses"])
    
plots.geometry_quantities(ideal_plain, ["intercept_factor","intercep_factorG"])


# plot_all_quantities(ideal_plain)
# plot_geometries_comparison([ideal_plain, virtual_abs], quantity="shadow_losses")
# plot_geometries_comparison(ideal_tr_dfs[:2], quantity="IAM")

# plot_geometries_comparison([errors_tr_dfs[0],ideal_tr_dfs[0]], quantity="IAM")
# plot_geometries_comparison([errors_ln_dfs[1],ideal_ln_dfs[0]], quantity="IAM")

# for tr in ideal_transversal_traces:
#     plot_heatmap(tr)

# for ln in ideal_longitudinal_traces:
#     plot_heatmap(ln)


# plot_geometries_comparison(ideal_tr_df_list[-2])
