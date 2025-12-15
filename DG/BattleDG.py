import CharecterDG
import random
import ActionsDG
import MapDG
Var = 0
def battle(place,Alive,spaceBuilding,spacePlace,mosters,Char,exit):
    global Var
    MapDG.os.system('clear') 
    Space = 0
    ran = random.randint(0,3)
    monster = mosters[Space][ran].split(':')
    
    

    
    if CharecterDG.EquipedWeapon == []:
        ActionsDG.Inputs.Var = 2
        input("You were killed, you forgot to equip a weapon \n press any key to continue")
        
    
    else:
        print(monster[0])

    
    

            





    




