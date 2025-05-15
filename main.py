# this will be our main module
from ts import getDate
from ts import getTimeStamp
# from ts import getDate, getTimeStamp
from util import makeInt

def main():
    ''' we often write a main module'''
    d = getDate()
    t = getTimeStamp()
    i = makeInt(42.24)
    print(d, t, i)

if __name__ == '__main__':
    main()