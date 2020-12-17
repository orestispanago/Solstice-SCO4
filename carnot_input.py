import pandas as pd
import numpy as np


df = pd.read_csv("export/annual-tilt38/raw/Annualall.csv", 
                 index_col="time", 
                 usecols=[0,5], 
                 parse_dates=True)

dr = pd.date_range(start="2016-01-01 00:00:00+00:00", end="2016-12-31 23:59:00+00:00", freq='1min', name='Time')
df = df[~df.index.duplicated(keep='last')]
df = df.reindex(dr)
df['s']=df.index.astype(np.int64) // 10**9 # datetime to seconds
df.set_index("s", inplace=True)

df.to_csv("absorbed_flux_2016.csv")
