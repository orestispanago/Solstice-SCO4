import pandas as pd
from config import trace


tr_args = trace.transversal.values()

columns = {"potential_flux": 2,
           "absorbed_flux": 3,
           "cos_factor": 4,
           "shadow_losses": 5,
           "missing_losses": 6,
           "reflectivity_losses": 7,
           "absorptivity_losses": 8
           }


def get_trace_attrs(df, trace):
    df.trace_geometry = trace.title.split(" ")[1]
    df.trace_direction = trace.title.split(" ")[0]
    return df

# TODO check calculation with partners
def calc_intercept_factor(df):
    df["intercept_factor"] = df["absorbed_flux"]/ (df["potential_flux"] * df["cos_factor"])
    
def calc_iam(df):
    df["IAM"] = df["intercept_factor"] / df["intercept_factor"][0]

def read(trace):
    if trace.df is not None:
        df = trace.df
    else:
        df = pd.read_csv(trace.rawfile, sep='\s+', names=range(47))
    trace_df = df.loc[df[1] == 'Sun', [trace.sun_col]]  # set 4 for longitudinal
    trace_df.columns = ["angle"]
    trace_df["efficiency"] = df.loc[df[0] == 'absorber', [23]].values  # Overall effficiency, add [23,24] for error
    for key in columns.keys():
        trace_df[key] = df[0].iloc[trace_df.index + columns.get(key)].astype('float').values
    trace_df = trace_df.set_index("angle")
    if trace.name == "Transversal":
        trace_df.index = trace_df.index-90
    calc_intercept_factor(trace_df)
    calc_iam(trace_df)
    return get_trace_attrs(trace_df, trace)


def read_mean(trace):
    trace_df = pd.read_csv(trace.meanfile)
    return get_trace_attrs(trace_df, trace)
