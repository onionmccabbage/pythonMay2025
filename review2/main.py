# this is main.py
import sys
import json
from swapi_service import SwapiService
from people import People
from planets import Planets
from species import Species

class Menu: # I chose not to descend from the Thread class, but I can still call 'run()'
    categories = ('people', 'planets', 'species', 'vehicles')
    def __init__(self):
        self.menu_choices = {
            "1":self.getPeople,
            "2":self.getPlanets,
            "3":self.getSpecies,
            "0":self.quit
        }
    def showMenu(self):
        print('''Choose an option:
        1: get people
        2: get planets
        3: get species
        0: quit
        ''')

    def run(self):
        while True: # a run-loop
            self.showMenu()
            choice = input('option? ')
            action = self.menu_choices.get(choice)
            if action:
                action() # this is a closure!
            else:
                print("{} is not a valid option".format(choice))

    def getId(self):
        self.which_id = int(float(input('which number? '))) # cast the string to an int
        # check an int was entered
        if type(self.which_id) == int and 0<self.which_id<7:
            return self.which_id
        else:
            return 1 # default to id 1

    def getPeople(self):
        self.category = 'people'
        result_d = SwapiService.getSwapi(self.category, self.getId())
        self.people = People(result_d['name'], result_d['height'])
        result = f"Name: {self.people.name} Height: {self.people.height}cm\n"
        print(result)
        self.appendData(result)

    def getPlanets(self):
        self.category = 'planets'
        result_d = SwapiService.getSwapi(self.category, self.getId())
        self.planets = Planets(result_d['name'], result_d['population'])
        print (f"Name: {self.planets.name} Population: {self.planets.population}")

    def getSpecies(self):
        self.category = 'species'
        result_d = SwapiService.getSwapi(self.category, self.getId())
        self.species = Species(result_d['name'], result_d['classification'])
        print (f"Name: {self.species.name} Classification: {self.species.classification}")

    def quit(self):
        sys.exit(0)

    def appendData(self,data_str):
        with open('swapi.txt', 'at') as fout:
            fout.writelines(data_str)

if __name__ == "__main__":
    Menu().run()