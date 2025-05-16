import doctest

def cubeIt(a,b):
    '''return sll the cube valiues between a and b
    Doctest lets us write ttests in this doc string
    >>> cubeIt(3, 6)
    [27, 64, 125]
    '''
    answers = []
    for i in range(a,b):
        answers.append( i**3 )
    return answers

if __name__ == '__main__':
    # print(  cubeIt(3,6) )
    doctest.testmod(verbose=True)