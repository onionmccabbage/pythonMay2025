# we may choose to write functions

def fnA(): # we define a function and start a code block with a colon
    a=3
    b=8.5
    return b/a # or + - * as usual

def fnB(a, b): # optionally a function may recieve variables (also called arguments)
    '''we often write a docstring to explain the purpose of a code block
    Triple quotes let us have new lines within a string object
    In this case, take a and b and calculate mathematical results'''
    # NB any arguments passed in to a function are local to this function
    total = a+b
    diff  = a-b
    prod  = a*b
    pow   = a**b
    modulo= b//a # modulo arithmetic - show integer division
    rem   = b%a  # show the remainder after integer division
    return (total, diff, prod, pow, modulo, rem) # a tuple of all my results

# demo alternative
def fnAlt(a, b): 
    r = {}
    r['total'] = a+b
    r['diff']  = a-b
    r['prod']  = a*b
    r['pow']   = a**b
    r['modulo']= b//a # modulo arithmetic - show integer division
    r['rem']  = b%a  # show the remainder after integer division
    return r
    # return f'{r['total']}{r['diff']}{r['prod']}{}{}{}'

def fnC(x=3, y=4): # we may choose to provide default values for any arguments
    '''calculate the hypotenuse given x and y'''
    h = (x**2+y**2)**0.5 # raise to **0.5 is the square root
    return f'The hypotenuse of {x} and {y} is {h}'

if __name__ == '__main__':
    # we may call the function
    r = fnA() # the () invoke the function (it runs)
    print( r, type(fnA) )  

    print( fnB(3, 12.9) )

    print(fnAlt(4,5))

    # we may call a function and use its defaults
    print( fnC() ) # 5.0
    # or we may override the defaults
    print( fnC(-3, -4) )

    # we may ask the user to provide data
    v = input('please enter a value: ') # careful EVERY input is ALWAYS a string
    print(v, type(v)) # always a string
    # we may attempt type-casting
    n = float(v)
    i = int(n)
    print(n, type(n), i, type(i))