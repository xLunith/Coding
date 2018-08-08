import random


class item():
    name = ''
    hp = 1


class weapon():

    atk = 0

    def __init__(self, name, hp, atk):
        self.name = name
        self.maxHp = hp
        self.atk = atk


class armor():

    ac = 0

    def __init__(self, name, hp, ac):
        self.name = name
        self.maxHp = hp
        self.ac = ac
