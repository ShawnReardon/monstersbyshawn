import copy
import random
from monster import *
from game import *



monsterDictionary = {
'weavile': Monster ('Weavile', 150), #change the hp to more than 150 if you want to win
'garchomp': Monster ('Garchomp', 250),
'roserade': Monster ('Roserade', 160),
'ambipom': Monster ('Ambipom', 160) 
}


me = Trainer('You', monsterDictionary['weavile']) #or choose ambipom to win
cynthia = Trainer('Cynthia', monsterDictionary['garchomp'])


new_game = Game(monsterDictionary)
#new_game.mainLoops()
new_game.battle()





