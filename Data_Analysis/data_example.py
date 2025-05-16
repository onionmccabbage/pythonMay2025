import numpy as np
import pandas as pd

# we can load external data
# Any data source is good: xls, xlsx, csv, html,.....
# Careful - the path must be relative to where we run Python
df = pd.read_csv('./Data_Analysis/data/Salaries.xls')
print(df.describe())

# If the data is large, it will be truncated
print(df.head(12)) # or df.tail(13)

# info about....
print(df.columns, df.size, df.max())
print(f"the mean salary is {df['salary'].mean():0.2f}")

# underlying iloc - the underlying index ordinal value
print(df.iloc[3][['salary']])

# Group and aggregate
df_rank = df.groupby(['rank'])
print(df_rank) # we have a 'groupBy' object which we can further use
print(df_rank.count())
# further analysis
df_n = df.groupby(['sex', 'salary'])
print( df_n.max() )
# mini-challenge
# find the mean years of service per rank
df_years = df.groupby('rank')
# CAREFUL - [[]] is a lsit [] inside a slice []
print( df_years[['service']].mean() ) # this shows just the service column mean()

# find the mean salary for all people earning over 120000
m = df[ df['salary']>120000 ]
print( '----------', m[['salary']].mean() )

# aggregration
df[[]]