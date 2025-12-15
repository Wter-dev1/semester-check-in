import random
import os
import CharecterDG

def Initial(size,space,spaceBuilding,spacePlace):
    for i in range(size):
        templist = []
        for r in range(size):
            templist.append("□")
        space.append(templist)



    for i in range(len(spaceBuilding)):
        GetType = spaceBuilding[i].split(':')
        PlacementData = GetType[0].split('-')
        buildinfo = [int(GetType[1]), int(PlacementData[0]),int(PlacementData[1]),int(GetType[2])]

        if buildinfo[0] == 1:
            for i in range((10 * 2) + 1):
                space[buildinfo[1] -10 ][buildinfo[2] - 10  + i] = '#'

                space[buildinfo[1] + 10 ][buildinfo[2] - 10  + i] = '#'
        
                space[buildinfo[1] - 10 + i][buildinfo[2] - 10] = '#'

                space[buildinfo[1] - 10 + i][buildinfo[2] + 10] = '#'

            space[buildinfo[1]][buildinfo[2] + 10] = '0'
            space[buildinfo[1]][buildinfo[2] - 10] = '0'
            space[buildinfo[1] - 10][buildinfo[2]] = '0'
            space[buildinfo[1] + 10][buildinfo[2]] = '0'    
            
            for i in range(buildinfo[3]):
                space[buildinfo[1] - 10 + random.randint(1,19)  ][buildinfo[2] - 10 + random.randint(1,19)  ] = 'M'
            for i in range(10 * 10 + 1 ):    
                spacePlace.append(int(PlacementData[0]) - 10 + int(PlacementData[1]) - 10 + i)


        if buildinfo[0] == 2:
            for i in range(10):
                space[buildinfo[1] -5 ][buildinfo[2] - 5  + i] = '#'

                space[buildinfo[1] + 5 ][buildinfo[2] - 5  + i] = '#'

                space[buildinfo[1] - 5+ i][buildinfo[2] - 5] = '#'

                space[buildinfo[1] - 5 + i][buildinfo[2] + 5] = '#'

            space[buildinfo[1] + 5 ][buildinfo[2]] = '0'

            space[buildinfo[1] - 3 ][buildinfo[2]] = '☒'

        if buildinfo[0] == 3:
            for i in range(12):
                space[buildinfo[1] -12 ][buildinfo[2] - 5  + i] = '#'

                space[buildinfo[1] + 5 ][buildinfo[2] - 12  + i] = '#'

                space[buildinfo[1] - 5+ i][buildinfo[2] - 5] = '#'

                space[buildinfo[1] - 12 + i][buildinfo[2] + 12] = '#'
            
            space[buildinfo[1] + 5 ][buildinfo[2]] = '0'
            for i in range(buildinfo[3]):
                space[buildinfo[1] - 12 + random.randint(1,11)  ][buildinfo[2] - 10 + random.randint(1,11)  ] = 'M'
            for i in range(10 * 10 + 1 ):    
                spacePlace.append(int(PlacementData[0]) - 12 + int(PlacementData[1]) - 12 + i)




def scrn(space,place,veiwSize):
    
    os.system('clear')

    space[place[0]][place[1]] = "X"
    

    for i in range((veiwSize * 2) ):
        print(str(space[i + (place[0] - veiwSize)][(place[1] - veiwSize) : (place[1] + veiwSize)]).replace("'","").replace("]","").replace("[","").replace(",",""))
    
    CharecterDG.ShowhealthNstuff()

def MUpd(space,spaceBuilding,clock):
    if clock % 150 == 0:
        for i in range(len(spaceBuilding)):
            GetType = spaceBuilding[i].split(':')
            PlacementData = GetType[0].split('-')
            buildinfo = [int(GetType[1]), int(PlacementData[0]),int(PlacementData[1]),int(GetType[2])]

            if buildinfo[0] == 1:
                
                for i in range(buildinfo[3]):
                    space[buildinfo[1] - 10 + random.randint(1,19)  ][buildinfo[2] - 10 + random.randint(1,19)  ] = 'M'
    
            if buildinfo[0] == 2:

                for i in range(buildinfo[3]):
                    space[buildinfo[1] - 5 + random.randint(1,9)  ][buildinfo[2] - 5 + random.randint(1,9)  ] = 'M'