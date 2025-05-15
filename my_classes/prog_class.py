# we may choose to define our own classes
# these can encapsulate rigour, such as validation and sanity

class Simple(): # the brackets are optional
    '''usually a class will initialize
    name must be a non-empty string'''
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

class Digital(Simple): # this new clas inherits all the capabilities of the parent class
    '''we extend the simple class to include attributes related to digital'''
    def __init__(self, name, episode, filesize):
        super().__init__(name, episode)
        self.filesize = filesize

# we may create instances of our class
s1 = Simple('Play School', 32)
s2 = Simple('News', 5667)
print(s1, type(s1), s1.name, s1.episode)

d1 = Digital('Prog', 34, 564745664)

# this is just like making any other class
l1 = []
t1 = (1,2,3)