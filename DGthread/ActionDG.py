import MapDG
import random
vision = ""
wall = ['#','█']



def Inputs(place,space,Char,Key,items):
    Inputs.Var = 0
    global vision
    global wall
    
    
    
    if Key == "w": 
        vision = space[place[0] - 1][place[1]] 
        place[0] = place[0] - 1
        space[place[0] + 1][place[1]] = ' '
        if space[place[0]][place[1]] in wall:
            place[0] = place[0] + 1      
    if Key == 'd': 
        vision = space[place[0]][place[1] + 1]
        place[1] = place[1] + 1
        space[place[0]][place[1] - 1] = ' '
        if space[place[0]][place[1]] in wall:
            place[1] = place[1] - 1
    if Key == 's': 
        vision = space[place[0] + 1][place[1]] 
        place[0] = place[0] + 1
        space[place[0] - 1][place[1]] = ' '  
        if space[place[0]][place[1]] in wall:
            place[0] = place[0] - 1      
    if Key == 'a': 
        vision = space[place[0]][place[1] - 1]
        place[1] = place[1] - 1
        space[place[0]][place[1] + 1] = ' '
        if space[place[0]][place[1]] in wall:
            place[1] = place[1] + 1

    if Key == '?':
        MapDG.os.system('cls') 
        print(" type p to stop and save your run.\n type f to see your inventory.\n type r to use a item without doing battle.\n (wasd to move around)")
        input("press any key when you are done").lower

    if Key == 'p':
        Inputs.Var = 1

    
    if Key == "f":
        print(items)

def stateUPDS(ItemDrops,items):
    global vision
    
    if vision == 'M':
        #BattleDG.battle(place,Alive,spaceBuilding,spacePlace,mosters,Char,exit)
        x=2
    if vision == '☒':
        items = "".join([str(items),str(ItemDrops[random.randint(0,len(ItemDrops) - 1)])])
        
        

    vision = ''