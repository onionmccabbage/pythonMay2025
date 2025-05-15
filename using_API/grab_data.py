# we may use the requests library to grab data from the internet
# we will use this URL
# https://jsonplaceholder.typicode.com/users/1

import requests # we may need to pip install requests


def getData():
    '''fetch some JSON from an API'''
    apiURL = 'https://jsonplaceholder.typicode.com/users/1'
    response = requests.get(apiURL) # we now have a response object
    # the response object will contain a status code, headers, the URL and our data
    # data may be JSON, HTML, Text, XML ....
    data = response.json() # since our data is JSON this will give us what we need
    return data

if __name__ == '__main__':
    user = getData()
    print(user)
