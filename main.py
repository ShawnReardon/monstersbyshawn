import copy
import random
from monster import *
from game import *

import csv
 
# opening the CSV file
with open('monsters.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)



monsterDictionary = {
'weavile': Monster ('Weavile', 150), #change the hp to more than 150 if you want to win
'garchomp': Monster ('Garchomp', 250),
'roserade': Monster ('Roserade', 160),
'ambipom': Monster ('Ambipom', 160) 
}

monsterList = list(monsterDictionary.items())


me = Trainer('You', monsterDictionary['weavile']) #or choose ambipom to win
cynthia = Trainer('Cynthia', monsterDictionary['garchomp'])


new_game = Game(monsterDictionary, monsterList)
#new_game.mainLoops()
new_game.battle()





