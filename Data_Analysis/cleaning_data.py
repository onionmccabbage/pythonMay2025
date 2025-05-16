import numpy as np
import pandas as pd

# we sometimes have incomplete data
d = ['A', 'B', np.nan, 'D']
y = pd.Series(d)
print(y.isnull()) # isna, notnull, notna


# what we can do...
print(y.fillna('Q')) # maybe use a meaningful value for missing - e.g. an average or median
# careful - almost all pandaas opersations oare non-descructive
print(y)

# this is a good idea - it helps maintain data integrity
# options = make a copy
z = y.fillna('Z') # we now have a new DataFrame
# or use 'implace'
y.fillna('Y', inplace=True) #this applies to DataFrame as well
print(y)
