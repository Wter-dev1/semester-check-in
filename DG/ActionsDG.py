import BattleDG
import CharecterDG 
import MapDG
import random
#ActionItems = ['□','☒','=','M','B']
wall = '#'
vision = ''



def Inputs(place,space,Char,Key):
    Inputs.Var = 0
    global vision
    
    Action = input(" Make your action: (type ? for help)").lower()
    
    if Action == 'w': 
        vision = space[place[0] - 1][place[1]] 
        place[0] = place[0] - 1
        space[place[0] + 1][place[1]] = '□'
        if space[place[0]][place[1]] == wall:
            place[0] = place[0] + 1      
    if Action == 'd': 
        vision = space[place[0]][place[1] + 1]
        place[1] = place[1] + 1
        space[place[0]][place[1] - 1] = '□'
        if space[place[0]][place[1]] == wall:
            place[1] = place[1] - 1
    if Action == 's': 
        vision = space[place[0] + 1][place[1]] 
        place[0] = place[0] + 1
        space[place[0] - 1][place[1]] = '□'  
        if space[place[0]][place[1]] == wall:
            place[0] = place[0] - 1      
    if Action == 'a': 
        vision = space[place[0]][place[1] - 1]
        place[1] = place[1] - 1
        space[place[0]][place[1] + 1] = '□'
        if space[place[0]][place[1]] == wall:
            place[1] = place[1] + 1

    if Action == '?':
        MapDG.os.system('clear') 
        print(" type ext to stop and save your run.\n type inv to see your inventory.\n type use to use a item without doing battle.\n (wasd to move around)")
        input("type done when you are done").lower

    if Action == "ext":
        Inputs.Var = 1
    if Action == "inv":
        CharecterDG.inv()
   
def Initial():
    global vision
    
    Inputs.Var = 0
    

def StateUPD(place,Alive,spaceBuilding,spacePlace,mosters,Char,exit,ItemDrops):
    global vision
    
    if vision == 'M':
        BattleDG.battle(place,Alive,spaceBuilding,spacePlace,mosters,Char,exit)
    if vision == '☒':
        NewItem = ItemDrops[random.randint(0,len(ItemDrops) - 1)]
        CharecterDG.lootBox(NewItem)
        input(NewItem)

    vision = ''
        
