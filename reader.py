import os
import pandas as pd

columns = {"potential_flux": 2,
           "absorbed_flux": 3,
           "cos_factor": 4,
           "shadow_losses": 5,
           "missing_losses": 6,
           # "reflectivity_losses": 7,
           # "absorptivity_losses": 8
           }


def get_direction_attrs(df, direction):
    df.direction_geometry = direction.geometry_name
    df.direction_name = direction.__class__.__name__
    return df


# TODO check calculation with partners
def calc_intercept_factor(df):
    df["intercept_factor"] = df["absorbed_flux"] / \
                             (df["potential_flux"] * df["cos_factor"])


def calc_iam(df):
    df["IAM"] = df["intercept_factor"] / df["intercept_factor"][0]


def read(direction):
    df = pd.read_csv(direction.csv_path, sep='\s+', names=range(47))
    direction_df = df.loc[df[1] == 'Sun', [direction.sun_col]]  # set 4 for longitudinal
    direction_df.columns = ["angle"]
    direction_df["efficiency"] = df.loc[df[0] == 'absorber', [23]].values  # Overall effficiency, add [23,24] for error
    for key in columns.keys():
        direction_df[key] = df[0].iloc[direction_df.index + columns.get(key)].astype('float').values
    direction_df = direction_df.set_index("angle")
    if direction.__class__.__name__ == "Transversal":
        direction_df.index = direction_df.index - 90
    calc_intercept_factor(direction_df)
    calc_iam(direction_df)
    return get_direction_attrs(direction_df, direction)


def read_list(directions):
    return [read(tr) for tr in directions]


def read_aggregate(direction, aggregate):
    mean_file = direction.csv_path.split(".")[0] + f"-{aggregate}.csv"
    direction_df = pd.read_csv(mean_file)
    return get_direction_attrs(direction_df, direction)
