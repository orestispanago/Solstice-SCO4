import pandas as pd

columns = {"potential_flux": 2,
           "absorbed_flux": 3,
           "cos_factor": 4,
           "shadow_losses": 5
           }

def get_trace_attrs(df, trace):
    df.label = trace.title.split(" ")[1]
    df.title = trace.title.split(" ")[0]
    df.xlabel = trace.xlabel
    return df

def read(trace):
    if trace.df is not None:
        df = trace.df
    else:
        df = pd.read_csv(trace.rawfile, sep='\s+',names=range(47))
    trace_df = df.loc[df[1] == 'Sun', [trace.sun_col]]  # set 4 for longitudinal
    trace_df.columns = ["angle"]
    trace_df["efficiency"] = df.loc[df[0] == 'absorber',[23]].values # Overall effficiency, add [23,24] for error
    for key in columns.keys():
        trace_df[key] = df[0].iloc[trace_df.index + columns.get(key)].astype('float').values
    trace_df = trace_df.set_index("angle")
    trace_df = get_trace_attrs(trace_df, trace)
    return trace_df
