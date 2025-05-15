# we may choose to define our own classes
# these can encapsulate rigour, such as validation and sanity

class Simple:
    '''usually a clas will initialize'''
    def __init__(self, name, episode): # all class functions take 'self' as an argument
        self.name = name
        self.episode = episode


# we may create instances of our class
s1 = Simple('Play School', 32)
s2 = Simple('News', 5667)
print(s1, type(s1), s1.name, s1.episode)


# this is just like making any other class
l1 = []
t1 = (1,2,3)