import CharecterDG
import MapDG
import ActionsDG
import threading



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

Key = ""

def Run():
    
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

    exit = False
    Alive = True

    with open("DG/DataStoreDG.txt",'r') as  file:
       content = file.read()
    
    SplitContent = content.split('/')
    mostersSplit = SplitContent[0].split('=')

    
    for i in range(len(mostersSplit)): mosters.append(mostersSplit[i].split(','))

    spaceBuildingSplit = SplitContent[1].split(",")
    spaceBuilding = []
    for i in range(len(spaceBuildingSplit)): spaceBuilding.append(spaceBuildingSplit[i])

    Char = SplitContent[2]

    PlaceSplit = SplitContent[3].split(",")
    place = [int(PlaceSplit[0]),int(PlaceSplit[1])]

    ItemDrops = SplitContent[4].split(",")






    ActionsDG.Initial()

    CharecterDG.initial(Char)
    CharecterDG.CharUPD(Char)

    MapDG.Initial(size,space,spaceBuilding,spacePlace)


    while exit == False:
        
        MapDG.MUpd(space,spaceBuilding,clock)
        MapDG.scrn(space,place,veiwSize)
        print(place)

        ActionsDG.Inputs(place,space,Char,Key)
        ActionsDG.StateUPD(place,Alive,spaceBuilding,spacePlace,mosters,Char,exit,ItemDrops)
        CharecterDG.CharUPD(Char)

        if ActionsDG.Inputs.Var == 2: exit = True ; Alive = False
        if ActionsDG.Inputs.Var == 1: exit = True
        

        clock = clock + 1
Run()
def LifeAfterDeath():
    if Alive == True:
        with open("DG/DataStoreDG.txt",'w') as  file:
            
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
            
        MapDG.os.system('clear')
        
        print("Game Saved:  Thanks for playing")
        MapDG.os._exit(0)
         
    else:
        MapDG.os.system('clear')
        input("Press any key to reload your last save")
LifeAfterDeath()

for i in range(100):
    Run()
    LifeAfterDeath()
    space = []
print("You have died too many times, \n its time you stop")

