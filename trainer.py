import copy
class Trainer(object):
    def __init__(self, name, *monster, human=False):
        self.name = name
        self.monster, self.monstername = [], []
        self.human = human
        for entity in monster:
            self.monster.append(copy.deepcopy(entity))
            self.monstername.append(entity.name)