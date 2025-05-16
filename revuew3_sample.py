# import 
import numpy as np
import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/ismayc/pnwflights14/master/data/flights.csv')
df = pd.read_csv('data/flights_jan.csv') # these two sources have different amounts of data

print( df.head() )

# how many elements this data has, the column names and the data types for each column)
print(df.size)
print(df.columns)
print(df.dtypes)

# Show the statistical summaries for the numeric columns in the dataset ( df.describe() )
print( df.describe() )

# Use the .agg() method to aggregate min, mean and max delays for departure and arrival
# We can use agg() methods for aggregation:
df[['DEPARTURE_DELAY','ARRIVAL_DELAY', 'DISTANCE']].agg(['min','mean','max', 'sum'])
# or
df.agg({'DEPARTURE_DELAY':['min','mean','max'], 'ARRIVAL_DELAY':['min', 'mean', 'max']})
# or
i = df[['DEPARTURE_DELAY', 'ARRIVAL_DELAY', 'DISTANCE']]
print( i.agg(['min', 'mean', 'max', 'sum']) )

# The number of flight records
df['FLIGHT_NUMBER'].count()


# The number of unique airlines
df.agg({'AIRLINE':['nunique']})

# How many unique aircraft are represented
df['TAIL_NUMBER'].nunique() 
# or 
df.TAIL_NUMBER.nunique()

# The greatest recorded delay (show the related data)
longest_delay = df.ARRIVAL_DELAY.max()
longest_delay
df[df.ARRIVAL_DELAY == longest_delay]

# A dataframe containing all AA flights that have no missing data members
df[df.AIRLINE == 'AA'].dropna()


# A dataframe containing all flights departing from SEA grouped by destination
# NB here we use mean() to show actual data rather than just the groupby object
df[df.ORIGIN_AIRPORT=='SEA'].groupby('DESTINATION_AIRPORT')[['DEPARTURE_DELAY']].mean() # nicely formatted data frame

# A dataframe containing all flights grouped by airline and sorted by increasing flight duration
result = df.groupby(['AIRLINE', 'FLIGHT_NUMBER'], sort=True)[['ARRIVAL_DELAY']].mean()
result

# punctuality meaning arrives on time or better
punct_arr = df[df['arr_delay']<=0]
punct_arr.max()
# punctuality meaning departs on time or better
punct_dep = df[df['dep_delay']<=0]
punct_dep.min()
# ... meaning arr and dep on time or better
punct = punct_arr[df['dep_delay']<=0]
punct.head()
# .. meaning arr and dep exactly on time
dep_ontime = punct[df['dep_delay']==0]
arr_ontime = dep_ontime[df['arr_delay']==0]
arr_ontime
dep_ontime

# ‐ Which airline arrives ahead of time most often
df_top = df.groupby(['carrier'])['arr_delay'].agg(len)
df_freq = df_top.sort_values(ascending=False).head(1).reset_index()
df_freq