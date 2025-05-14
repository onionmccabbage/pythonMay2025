# a run loop lets us keep a module running until we choose to end it
def game():
    while True:
        '''this loop will never end (unless we break out of it)'''
        cat = input('Please enter chosen category: ')
        if cat in {'news', 'sport', 'weather', 'iplayer'}:
            # when we wish to break out...
            print(f'You chose {cat}')
            break # the run loop stops

if __name__ == '__main__':
    game()