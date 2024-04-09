import random

class Hero:

    def __init__(self, name, hp, strength, Htype=None) :
        self.name = name
        self.hp = hp
        self.strength = strength
        self.Htype = Htype



class Monster:
    def __init__(self, Htype, hp, strength) :
        self.Htype = Htype
        self.hp = hp
        self.strength = strength
