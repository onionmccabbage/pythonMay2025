# We may read back from a file
def readfile():
    try:
        with open('my_file.txt', 'rt') as fin: # 'r' will read ('t' for text)
            retrieved = fin.read() # retrieve the entire contents
            return retrieved
    except Exception as err:
        print(err)

def readFileLines():
    '''retrieve the contents into a list of lines'''
    try:
        with open('my_file.txt', 'rt') as fin: # 'r' will read ('t' for text)
            retrieved = fin.readlines() # retrieve the entire contents as a list of lines
            return retrieved
    except Exception as err:
        print(err)

if __name__ == '__main__':
    r = readfile()
    print(r)
    l = readFileLines()
    print(l) # we have a list
    for i in l: # we may choose to iterate over this list to show each separate line
        print(i)