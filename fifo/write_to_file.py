import sys
# sometimes we need to write rather than print
# Whenever we deal with I/O bound events it is a good idea to use try/except
def commitTofile(txt): # we may choose to receive zero or more arguments
    '''write data to a text file'''
    try:
        # if there is a file name is sys.argv the use it
        if len(sys.argv) > 1:
            file_to_write = sys.argv[1]
        else:
            file_to_write = 'my_file.txt'
        # 'with' is a very tidy way to work with objects
        with open(file_to_write, 'at') as fout:
            fout.write(txt) # commit the incoming text to this file access object
            # we may choose ot add a new line character
            fout.write('\n') # \n is encoding for a new line. \t is tab
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