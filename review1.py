# Python review exercise: guess the random number between 0-100
import random # we need a way to make random numbers

def game():
    ''' ask user to guess a random integer 0-100 '''
    target = random.randint(0,100) # up to 100 inclusive
    # create collections of odds, evens, squares and primes
    odd_ints     = range(1, 100, 2) 
    even_ints    = range(0, 101, 2)

    primes_t = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    # set some boolean flags regarding the nature of our target number
    is_odd    = target in odd_ints
    is_even   = target in even_ints
    is_prime  = target in primes_t
    # keep the game running
    guess_counter = 0
    while True: # keep going!!
        guess_counter += 1
        # really should try-except here....!
        guess = int(float(input('guess:'))) # make sure it's an int
        # conditionally act on the guess
        if guess == -2: # do they want a clue
            print (f'CLUE: odd: {is_odd} even: {is_even} prime: {is_prime}' )
        elif guess == -1: # do they want to quit
            print (f'it was {target}' )
            guess = target # break # stops the current loop
            # break # break out of the function
            break
        elif guess > target: # is the guess too high
            print('too high')
            continue
        elif guess < target: # is the guess too low (could be an else clause)
            pass # just go to the next line
            print('too low')
            pass
        else:
            print(f'correct it was {target} you took {guess_counter} tries' )
            break

if __name__ == '__main__':
    game()
