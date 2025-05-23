import datetime

# the range object is extremely efficient
r = range(-10, 11, 2) # start, stop-before, step
for i in r:
    print(i)

# this is similar to 'slicing' for any ordinal collection
s = 'here is a string of text'
t = (True, 5,4,3, 'text', 'a', 'b', 'c')
print(s[2:9:2]) # [start:stop-before:step]
print(t[0:6])

# list comprehension
square_nums = [i**2 for i in range(0,101)]
print(square_nums)

# comprehension use-case
raw_data = (7,4,8,3,9,22,5)
# maybe we need the date representation of these numbers
dt = datetime.time(23)
print(dt)
dates_l = [datetime.time(i) for i in raw_data]
print(dates_l) # we have a nice list of actual time stamps
for dt in dates_l:
    print(dt)

# generator syntax
p = (i**2 for i in range(0,101)) # this is not a list, it is a generator
print(type(p))
# a generator lets us iterate over the generated members 
# but the members do not persist in memory
for i in p:
    print(i)

# use-cases
# generate the next id for a file/db/API etc
# automatically generate the next file name for storage/retrieval
names_g = (f'log_{i}.json' for i in range(0,11))
for i in names_g:
    print(i)

