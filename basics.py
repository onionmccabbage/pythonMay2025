# this is a comment
# Python files are just plain txt, known as modules
a = 3   # this is an integer
b = 8.7 # this is a floating point number
c = a+b
print(a, b, c) # output to the console

# other types of data
d = True # or False
e = None
# string is a zero-based immutable ordinal collection of characters
f = 'this is a string of characters' 
# we can change the value of any variable - this does not mutate it, it replaces it
f = 'is it time for coffee?'
print(f[8]) # 'a'
# list and tuple  
l = [3,4,5] # an ordinal mutable collection of any data types
t = (3,4,5) # an ordinal immutable collection of any data types
print( l, type(l), t, type(t), type(a), type(b) )
# we may alter a list
l[2] = 'changed'
l.append(t) # also remove() and insert()

print(l)

# two final collections: dictionary and set
# dict is a NON ORDINAL mutable collection of any data type
person = {'fn':'Floella', 'ln':'Benjamin', 'level':'Admin', 'data':l}
person['age']=72
person['level'] = 'super user'
print(person, type(person))

# a set is a non ordinal mutable collection of UNIQUE members (of any data type)
s = {4,5,6,7,7,7,8,9,0,7,7,3} # by default Python will sort the order ascending

print(s, type(s))

# iterating over collections (loops)
# CAREFUL - a colon begins a block of code. The block of code is indented
for i in t: # nothing special about 'i' 
    print(i)
for i in l:
    print(i)

# we can use a range to see members of a collection
for i in range(0,3): # range will start, stop-before,step
    print( l[i] )
print('backwards')
for i in range(3,0,-1): # loop backwards
    print(l[i] )

# the 'range' object is useful. it provides ranges of values without persisting them in memory.
# The values are generated on demand
# r = range(-10**100, 10**100, 100) # nb ** means raise to the power
# for i in r:
#     print(i)