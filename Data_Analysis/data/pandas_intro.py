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
s = pd.Series(l, index=ind)
print(s)

