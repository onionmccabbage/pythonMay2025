import numpy as np
import pandas as pd

# Yet more structures available in pandas
l = [9, 7.5, -5, 3, 99] # this is a list
# a pandas Series is a mutable ordinal indexed collection of one data type
p = pd.Series( l )
p[3] = np.nan # this represents 'not a number'
print(p, p.values, p.index)

# we may customize the index of a Series
ind = ('c', 'b', 'a', 'c', 'd') # this is a tuple
s = pd.Series(l, index=ind) # a Series may have a custom index
print(s)
# we can still use slicing, but it is stop, not stop-before
print( s['b':'d'] ) # from 'b' to 'd' inclusive

# we can find matching members
print(s['c']) # there are two matches
print(s[s>4])
# statistics
print( s.mean() )
print( s.min() )
print( s.max() )
print( s.count() )

# Pandas DataFrame is very similar to a spreasheet layout
# NB DataFrame is a collection of Series - each column is a pandas Series

# here is some data
sdata = {'Cork':35000, 'Dublin':71000, 'Galway':16000, 'Athlone':5000, 'Genoa':500} # dict
idata = {'Cork', 'Dublin', 'Shannon', 'Galway', 'Athlone'} # set
c = pd.Series(sdata, index=idata)
c['Shannon'] = 8888
print(c)

# some more data
towns_l = ['Cork', 'Dublin', 'Galway', 'Athlone', 'Shannon', 'Rosscarbery', 'Athenry']
years_l = [2017, 2018, 2019, 2020, 2021, 2022, 2023]
# years_l = y.sort()
# print(years_l)
pop_l   = [1.5, 1.7, 3.6, 2.4, 2.9, 3.2, 1.7]
# make a dict
data_d = {'Towns':towns_l, 'Years':years_l, 'Pop':pop_l}
# a DataFrame is an ordinal mutable colection of Series
df = pd.DataFrame(data_d, index=years_l)
print(df)
# we can access members by their column name
print( df[['Years', 'Pop']] )

# statistical analysis
print(df.describe())


# Can we sort the members (e.g. by index...)