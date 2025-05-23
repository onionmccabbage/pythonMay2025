# we may choose to define our own classes
# these can encapsulate rigour, such as validation and sanity

class Simple(): # the brackets are optional
    '''usually a class will initialize
    name must be a non-empty string
    episode must be a positive non-zero integer'''
    # slots let us li mit precicely which peroperties are permitted in this class
    __slots__ = ('__name', '__episode')
    def __init__(self, name, episode): # all class functions take 'self' as an argument
        self.name = name # here self.name will call the name setter function
        self.episode = episode
    # we write get/set methods as decorators
    @property
    def name(self): # this is the getter for 'name'
        '''we will return the current value for 'name' '''
        return self.__name # the double underscore is called 'name mangling'
    @name.setter
    def name(self, new_name): # this is the setter for 'name'
        '''only permit non-empty string'''
        if type(new_name)==str and new_name != '':
            self.__name = new_name
        else:
            raise TypeError('name must be a non-empty string')
    @property
    def episode(self): # this is the getter for 'episode'
        '''we will return the current value for 'episode' '''
        return self.__episode # the double underscore is called 'name mangling'
    @episode.setter
    def episode(self, new_episode): # this is the setter for 'episode'
        '''only permit non-zero positive integer'''
        if type(new_episode)==int and new_episode >0:
            self.__episode = new_episode
        else:
            raise TypeError('episode must be a positive integer')
    # many things in Python have __XXXX__ 
    # These all belong to Python. They are called 'dunder'
    # we may choose how this class should print
    def __str__(self): 
        '''we override the built-in __str__ method with our own code'''
        return f'This program is called {self.name} episode {self.episode}'

# we can create our own exception classes
class NotPosInt(TypeError):
    pass

class Digital(Simple): # this new clas inherits all the capabilities of the parent class
    '''we extend the simple class to include attributes related to digital'''
    def __init__(self, name, episode, filesize):
        super().__init__(name, episode)
        self.filesize = filesize

# we may create instances of our class
s1 = Simple('Play School', 32)
s2 = Simple('News', 5667)
s8 = Simple(episode=34, name='Demo')
# NB s.name will call the getter function for 'name'
print(s1, type(s1), s1.name, s1.episode)

# we can check if our validation is operating correctly
# an incorrect name
try:
    # s3 = Simple(True, 55) # True should not be permitted
    # s4 = Simple('totp', None) # none shoyuld not be permitted
    s5 = Simple('totp', -99) # -ve not be permitted
except TypeError as te:
    print(te)

# we can work with the class properties
s1.episode = 99 # this will call the setter method

d1 = Digital('Prog', 34, 564745664)

# this is just like making any other class
l1 = []
t1 = (1,2,3)