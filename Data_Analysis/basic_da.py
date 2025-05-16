# for data analysis we usually use these two libraries
# remember -we may need to pip isntall these
# py -3 -m pip install numpy
# py -3 -m pip install pandas
# or 
# python -m pip install numpy
# or
# pip install numpy

import numpy as np
import pandas as pd

# Numpy offers additional data structures
# the arange is an array-range object
n = np.arange(2,8,0.5) # all members must be the SAME data-type
print(n, n.dtype)

# we may need an array
m = np.random.randn(4,3)
print(m, m.dtype) # all members of an arange (an array) must be the same data type
print(m.shape)

# we may have more than two dimensions
e = np.random.randn(2,4,3,2)
print(e)

# careful when creating arrays
f = np.empty( (3,6) )
g = np.zeros( (3,6), 'int32' ) # we masy specify what data type to use
h = g.astype(np.str_) # str_ is the string type
print(f,g,h, h.dtype)

# usully data sourcces are large
z = np.random.randn(9999,9999)
# we may carry out operations on every member of an array, 'at the same time'
# powers = (z+3)**2
# print(z)

# we still have slicing....
print( z[0:5:2] )
# we still have access mutation
z[0,1] = 99
print(z[0,1])

print(f.T) # transpose the entire array