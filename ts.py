# this module can provide a date-time stamp when needed
from time import time # we have access to just the 'time' funcrionality fro mthis module
from datetime import * # this gives us access to everything inside the datetime module
# the above line is the same as import datetime

def getTimeStamp():
    return time() # this will be a large number preresenting a moment in time

def getDate():
    return datetime.date( datetime.today() )

if __name__ == '__main__':
    # we can exercise the code to make usre it operates as expected
    ts = getTimeStamp()
    d  = getDate()
    print(f'The time is {ts} the date is {d}')