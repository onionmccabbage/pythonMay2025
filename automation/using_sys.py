# we may inject data at the moment we run the module
import sys

print(sys.path) # all the places Python will look when importing

# sys includes argument variables (sys.argv)
# member zero of sys.argv is always the name of the module
print(sys.argv[0]) # what is this module called?
# we may choose to inject additional system argument variables
for i in sys.argv:
    print( i )

# to see this is operation:
# python using_sys.py add any variables
# then sys.argv[1] will contain 'add'
# then sys.argv[2] will contain 'any'
# then sys.argv[3] will contain 'variables'