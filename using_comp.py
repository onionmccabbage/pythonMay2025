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



# generator syntax


