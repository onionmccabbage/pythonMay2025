# Python review exercise: guess the random number between 0-100
import random # we need a way to make random numbers

def game():
    ''' ask user to guess a random integer 0-100 '''
    target = random.randint(0,100) # up to 100 inclusive
    while True: # keep going!!
        # really should try-except here....!
        guess = int(float(input('guess:'))) # make sure it's an int
        # conditionally act on the guess
        if guess == -1: # do they want to quit
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
            print(f'correct it was {target}' )
            break

if __name__ == '__main__':
    game()
