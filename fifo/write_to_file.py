# sometimes we need to write rather than print
# Whenever we deal with I/O bound events it is a good idea to use try/except
def commitTofile(txt): # we may choose to receive zero or more arguments
    '''write data to a text file'''
    try:
        # 'with' is a very tidy way to work with objects
        with open('my_file.txt', 'at') as fout:
            fout.write(txt) # commit the incoming text to this file access object
    except Exception as err:
        print(err)

def askUser():
    '''get some data from the user'''
    try:
        n = input('please enter data: ')
        return n # just send what the user entered back out
    except Exception as err:
        print(f'{err}')
    # we are not obliged to write a 'finally' block

if __name__ == '__main__':
    d = askUser()
    commitTofile(d)