# we may use the requests library to grab data from the internet
# we will use this URL
# https://jsonplaceholder.typicode.com/users/1

import requests # we may need to pip install requests
import sys

def getData(id=1):
    '''fetch some JSON from an API'''
    apiURL = f'https://jsonplaceholder.typicode.com/users/{id}'
    response = requests.get(apiURL) # we now have a response object
    # the response object will contain a status code, headers, the URL and our data
    # data may be JSON, HTML, Text, XML ....
    data = response.json() # since our data is JSON this will give us what we need
    return data # we have a dictionary containing the data
# () usually means a tuple
# [] usually means a list
# {} usually means a dict or a set

if __name__ == '__main__':
    # where to get arguments...
    # user input, read from file, get a sys.argv, grab from database....
    if len(sys.argv)>1:
        chosenID = sys.argv[1] # remembber member 0 is the file name
    else:
        chosenID = 3

    user = getData(chosenID) # we may choose to pass an id argument
    print(user)

    # we may grab elements of the dict
    print(user['name'])
    print(user['website'])
    # how would we access the company city?
    print( user['address']['city'] )
    print( user['address']['geo']['lat'] )
    print( user['address']['geo']['lng'] )

    for (k,v) in user.items():
        print(f'{k}:{v}')


