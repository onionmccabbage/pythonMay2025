# all names in Python may use letters, numbers and the underscore
# names CANNOT begin with a digit

# we may write a function like this 
def getInfo():
    '''we often write a docstring explaining the purpose
    Triple quotes let us greak our words over several lines
    This can aid with clarity'''
    # input stops and waits for the user to type something
    # CAREFYL 'input' will ALWAYS return a string value
    v = input('Please enter a value: ') # single equals SETS equality
    # conditional coding - act according to the entered value
    # first, can it be an integer
    # using exception handlers
    try:
        # NB we cannot go from a string that looks like a float directly to an int
        num = int(float(v)) # we try to cast the string to a number (int or float)
        print(f'Success - the number is {num}')
    except Exception as err:
        print(f'There was a problem: {err}')
    finally:
        print('the finally block always runs, whether or not we have an exception')
    if v.isnumeric(): # isnumeric will check if a string contains only digits
        n = int(v) # here we 'cast' the type from a string to an integer
        # use formatting to tidy up the values
        return f'The number {n} was entered' # f lets us inject valus into our string
    else:
        return f'The string {v} is not a number'

# this next line looks weird but is very common practice in Python
if __name__ == '__main__': # double-equals CHECKS equality
    # write our immediate code here
    s = getInfo() # this will invoke our function
    print(s, type(s))