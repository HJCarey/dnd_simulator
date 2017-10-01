import numpy as np


class Character extends Creature:

    #name = _
    #stats = _
    #c_class = _
    
    def __init__ (self, name):#, age, char_class, level):
        self.name = name
        self.stats = {}
        self.rand_skills()
        self.choose_class()
        
    def rand_skills(self):
        self.stats['str'] = np.random.randint(10,18)
        self.stats['dex'] = np.random.randint(10,18)
        self.stats['con'] = np.random.randint(10,18)
        self.stats['int'] = np.random.randint(10,18)
        self.stats['wis'] = np.random.randint(10,18)
        self.stats['cha'] = np.random.randint(10,18)
        
    def choose_class(self):
        print("Do stuff")
    
    def show_character(self):
        print("My name is %s" % self.name)
        for key, value in self.stats.items():
            print("%s: %d"%(key, value))