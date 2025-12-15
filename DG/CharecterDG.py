import MapDG

EquipedArmor = []
EquipedWeapon = []
ItemsToAdd = []

def initial(Char):
    #"jerry.100.sword:1:5,sheild:2:5"
    
    breaklist = Char.split('.')
    
    initial.name = breaklist[0]
    initial.hp = int(breaklist[1])
    initial.totalHp = initial.hp
    initial.items = breaklist[2].split(',')
    initial.armor = []
    initial.weapons = []
    initial.consumables = []

    for i in range(len(initial.items)):
        itemInfo = initial.items[i].split(":")

        if int(itemInfo[1]) == 1:
            initial.weapons.append(itemInfo[0])
            initial.weapons.append(int(itemInfo[2])) 
        if int(itemInfo[1]) == 2:
            initial.armor.append(itemInfo[0])
            initial.armor.append(int(itemInfo[2]))
        if int(itemInfo[1]) == 3:
            initial.consumables.append(itemInfo[0])
            initial.consumables.append(int(itemInfo[2]))

def CharUPD(Char):
    global ItemsToAdd
    breaklist = Char.split('.')
    
    CharUPD.name = breaklist[0]
    CharUPD.hp = int(breaklist[1])
    CharUPD.totalHp = initial.hp
    CharUPD.items = breaklist[2].split(',')
    if len(ItemsToAdd) > 0:
        CharUPD.items.append(str(ItemsToAdd).replace('[','').replace(']','').replace('"','').replace("'",''))
        
    CharUPD.armor = []
    CharUPD.weapons = []
    CharUPD.consumables = []

    for i in range(len(CharUPD.items)):
        itemInfo = CharUPD.items[i].split(":")

        if int(itemInfo[1]) == 1:
            CharUPD.weapons.append([itemInfo[0],itemInfo[2]])
  
 
        if int(itemInfo[1]) == 2:
            CharUPD.armor.append([itemInfo[0],itemInfo[2]])

        if int(itemInfo[1]) == 3:
            CharUPD.consumables.append([itemInfo[0],itemInfo[2]])

def inv():
    global EquipedWeapon
    global EquipedArmor

    MapDG.os.system('clear')

    print("\033[1m Weapons\033[0m")
    for i in range(len(CharUPD.weapons)):
        print(str(CharUPD.weapons[i][0]).replace("[","").replace("]","").replace('"',"").replace("'","").replace(" ",""), i + 1)

    print("\033[1m Armor\033[0m")
    for i in range(len(CharUPD.armor)):
        print(str(CharUPD.armor[i][0]).replace("[","").replace("]","").replace('"',"").replace("'","").replace(" ",""), i + 1)
    
    print("\033[1m Consumables\033[0m")
    for i in range(len(CharUPD.consumables)):
        print(str(CharUPD.consumables[i][0]).replace("[","").replace("]","").replace('"',"").replace("'","").replace(" ",""), i + 1)

    huh = input("Would you like to equip a weapon or armor (type W or A) : ").lower()

    if huh == "w":
        inde = int(input("choose which weapon you want (put in the number in front of the weapon) : "))
        EquipedWeapon = CharUPD.weapons[inde - 1]


    elif huh == "a":
        
        inde = int(input("choose which Armor you want to equip (put in the number in front of the armor peice) : "))
        EquipedArmor = CharUPD.armor[inde - 1]

def lootBox(NewItem):
    global ItemsToAdd
    ItemsToAdd.append(NewItem)    
    
def ShowhealthNstuff():
    print("HP = ",CharUPD.hp,'/',CharUPD.totalHp)

    if EquipedWeapon == []:
        print("Weapon: Nothing")
    else:
        print("Weapon: ", EquipedWeapon[0]," +Damage: ",EquipedWeapon[1]) 
        

    if EquipedArmor == []:
        print("Armor: Nothing")
    else:
        print("Armor: ", EquipedArmor[0]," +Protection: ",EquipedArmor[1]) 
        


