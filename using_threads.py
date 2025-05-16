# threading lets us do several things at the same time
from threading import Thread
import random
import time

def myfn(n):
    '''sleep for a random amount of time'''
    for i in range(0,5):
        print(f'{n} is sleeping')
        time.sleep( random.random()*0.1 ) # sleep for up to a tenth of a second

if __name__ == '__main__':
    # we can carry out many concurrent operations
    # sequential
    s1 = time.time()
    myfn(1)
    myfn(2)
    myfn(3)
    myfn(4)
    myfn(5) # up to 2.5 seconds
    s2 = time.time()
    print(f'total time: {s2-s1}')
    #concurrent
    s1 = time.time()
    t1 = Thread(target=myfn, args=(1,))
    t2 = Thread(target=myfn, args=(2,))
    t3 = Thread(target=myfn, args=(3,))
    t4 = Thread(target=myfn, args=(4,))
    t5 = Thread(target=myfn, args=(5,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    # we may want the main thread to wait for other threads to complete before moving on
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    s2 = time.time()
    print(f'total time: {s2-s1}')