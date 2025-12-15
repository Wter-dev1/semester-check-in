import msvcrt
import threading
import time
import os
import MapDG
import ActionDG
ItemDrops = []
mosters = []
spaceBuilding = []
Char = ""
place = []
spacePlace = []
space = []
size = 1000
veiwSize = 10
exit = False
Alive = True
clock = 0
name =""
totalhp =0
hp =0

itemInfo = []

items = ''
armor =[]
weapons =[]
consumables =[]
Key = ""

def Reader():
    global mosters 
    global spaceBuilding
    global Char
    global place
    global ItemDrops
    global spacePlace 
    global space 
    global size
    global veiwSize 
    global exit 
    global Alive 
    global clock 
    global name 
    global totalhp 
    global hp 
    global items 
    global armor 
    global weapons 
    global consumables 
    global itemInfo


    with open("DataStoreDG.txt",'r') as  file:
       content = file.read()
    
    SplitContent = content.split('/')
    mostersSplit = SplitContent[0].split('=')

    
    for i in range(len(mostersSplit)): mosters.append(mostersSplit[i].split(','))

    spaceBuildingSplit = SplitContent[1].split(",")
    spaceBuilding = []
    for i in range(len(spaceBuildingSplit)): spaceBuilding.append(spaceBuildingSplit[i])

    Char = SplitContent[2]
    breaklist = Char.split('.')
    
    name = breaklist[0]
    totalhp = int(breaklist[1])
    hp = totalhp
    items = breaklist[2].split(',')
    armor = []
    weapons = []
    consumables = []

    
    PlaceSplit = SplitContent[3].split(",")
    place = [int(PlaceSplit[0]),int(PlaceSplit[1])]

    ItemDrops = SplitContent[4].split(",")

def ChrUpd():
    global name 
    global totalhp 
    global hp 
    global items 
    global armor 
    global weapons 
    global consumables 
    
    
    weapons = []
    armor = []
    consumables = []
    
    for i in range(len(items)):
        itemInfo = items[i].split(":")

        if int(itemInfo[1]) == 1:
            weapons.append(itemInfo[0])
            weapons.append(int(itemInfo[2])) 
        if int(itemInfo[1]) == 2:
            armor.append(itemInfo[0])
            armor.append(int(itemInfo[2]))
        if int(itemInfo[1]) == 3:
            consumables.append(itemInfo[0])
            consumables.append(int(itemInfo[2]))
    


def Save():
    with open("DataStoreDG.txt",'w') as  file:
            
            file.write(str(mosters[0]).replace("[","").replace("]","").replace('"',"").replace("'","").replace(" ",""))
            for i in range(len(mosters) - 1):
                file.write("=")
                file.write(str(mosters[i + 1]).replace("[","").replace("]","").replace('"',"").replace("'","").replace(" ",""))


            file.write("/")
            file.write(str(spaceBuilding).replace("[","").replace("]","").replace('"',"").replace("'","").replace(" ",""))
            file.write("/")
            file.write(str(Char).replace("[","").replace("]","").replace('"',"").replace("'","").replace(" ",""))
            file.write("/")
            file.write(str(place).replace("[","").replace("]","").replace('"',"").replace("'","").replace(" ",""))
            file.write("/")
            file.write(str(ItemDrops).replace("[","").replace("]","").replace('"',"").replace("'","").replace(" ",""))

def KeyGet(name, delay):
    global Key
    key_as_bytes = msvcrt.getch()
    Key = key_as_bytes.decode('utf-8')



def GameLoop():
    global mosters 
    global spaceBuilding
    global Char
    global place
    global ItemDrops
    global spacePlace 
    global space 
    global size
    global veiwSize 
    global exit 
    global Alive 
    global clock 

    Reader()

    for i in range(size):
        templist = []
        for r in range(size):
            templist.append(' ')
        space.append(templist)
    MapDG.Initial(size,space,spaceBuilding,spacePlace)

    space[500][500] = '▒'

    while exit == False:
    
    
        thread_name = "thread"
        thread = threading.Thread(target=KeyGet, args=(thread_name,10))
        
    
        thread.start()
        MapDG.Scrn(space,place,veiwSize)
    
        print(place)
        print("press ? for help")
        

    

        time.sleep(0.01)
    
    

        thread.join()
    
        os.system('cls')
        ActionDG.Inputs(place,space,Char,Key,items)
        ActionDG.stateUPDS(ItemDrops,items)
        
        if ActionDG.Inputs.Var == 2: exit = True ; Alive = False
        if ActionDG.Inputs.Var == 1: exit = True
def AfterLoop():

    if Alive == False:
        input("you died press any key to reload your last save")

    else:
        Save()
        os.system('cls')
        
        print("Game Saved:  Thanks for playing")
        os._exit(0)

for i in range(100):
    GameLoop()
    AfterLoop()






    

