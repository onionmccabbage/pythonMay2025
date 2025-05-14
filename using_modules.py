# we may import from other modules
import random

print(random.randint(0,10))

primes_t = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

def checkValue():
    '''check the value of a random number'''
    r = random.randint(0,100)
    if r in primes_t:
        print(f'The number {r} is a prime number')
    if r>50:
        # print (f'{r} is greater than 50')
        return f'{r} is greater than 50'
    elif r<=50:
        return f'{r} is 50 or less'
    else:
        return 'not known'
    


    
if __name__ == '__main__':
    c=checkValue()
    print(c)