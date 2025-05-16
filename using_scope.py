# python has 'scopes'
# the global scope is all code not inside a code block
# each code block has its own local scope

# NB generally we avoid polluting the global namespace/scope

g = 'this is in the global scope'

def fn():
    '''this function has its own local scope'''
    # if we wish, we may access global assets inside a local scope
    global g # we now have access to the 'g' in the global scope
    g = 'inside the function'
    return g

if __name__ == '__main__':
    print(g)
    print( fn() )
    print(g) # changed by the function




