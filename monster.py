class Monster(object):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def attack(self, oponent):
        oponent.hp = oponent.hp - 150 #just for a test