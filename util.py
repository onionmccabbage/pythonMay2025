# here we write a useful utility

def makeInt(n):
    '''if a valid number is provided, return the integer part
    for invalid values, return zero'''
    if type(n) in (int, float):
        return int(n)
    else:
        return 0