import random
from trainer import *
def alive(monster): #check if the monster is alive
    if monster.hp>0:
        return True
    if monster.hp<=0:
        monster.hp=0
        return False
      
class Game:
  def __init__(self, monsterDictionary, monsterList):
    self.trainer1 = None
    self.trainer2 = None
    self.monsterDictionary = monsterDictionary
    self.monsterList = monsterList
    self.createTrainers()

  def createTrainers(self):
    trainer1Name = input("Input Trainer 1's name: ")
    is_human =input("Is Trainer1 Human, Y or N ")
    if is_human not in ('Y', 'y', 'N', 'n'):
      print('Not Valid Input')
   
    self.trainer1 = Trainer(trainer1Name, self.monsterDictionary['garchomp'])
    trainer2Name = input("Input Trainer 2's name: ")
    is_human =input("Is Trainer2 Human, Y or N ")
    if is_human not in ('Y', 'y', 'N', 'n'):
      print('Not Valid Input')
    self.trainer2 = Trainer(trainer2Name, self.monsterDictionary['garchomp'])
      
    


  #def mainLoops(self):
  def battle(self): #battle between two trainers
      fight1, fight2 = True, True
      i = 0
      while fight1 and fight2:
        print ('Choose a monster: ')
        for item in self.monsterList:
          print(i+1, self.monsterList[i][0])
          i += 1
        monster1 = self.monsterDictionary[self.monsterList[int(input())-1][0]]
        while not alive(monster1):
            print (monster1.name, 'is out of batlle. Choose another monster')
            monster1 = eval(input())
        monster2 = random.choice(self.trainer2.monster)
        while not alive(monster2):
            monster2 = random.choice(self.trainer2.monster)
        print (self.trainer1.name, 'chose', monster1.name, '\n', self.trainer2.name, 'chose', monster2.name)
        while alive(monster1) and alive(monster2):
            monster1.attack(monster2)
            if alive(monster2):
                monster2.attack(monster1)
            print (monster1.name, monster1.hp)
            print (monster2.name, monster2.hp)
        print (self.trainer1.monster[0].name, self.trainer1.monster[0].hp) #here its returning the original hp
        print (self.trainer2.monster[0].name, self.trainer2.monster[0].hp) #here its returning the current hp, as it should
        if not any(alive(monster) for monster in self.trainer1.monster):
            fight1 = False
        if not any(alive(monster) for monster in self.trainer2.monster):
            fight2 = False

   