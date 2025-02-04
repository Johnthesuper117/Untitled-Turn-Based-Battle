#debug game and make sure every move works as intended, send to uncle Tim and David to test and give feedback, afterwards add finishing touches and last wave of testing, then release as finished version

#import stuff
import time
import random

#intro, rules, and how to play
print("Hello and Welcome to Untitled Turn-Based Battle version Alpha")
time.sleep(1)
print("\nHow to play:\nFirst, before the battle starts, you select one attack for each category: Weapon, Spell, Shield, Potion, and Finisher. \nDuring the battle, you get to choose your attacks until you run out of stamina points. Then, your opponent does the same. This continues until one of the players lose all of their health, the one who remains is the winner!")
time.sleep(3)
print("\nRules: Both players have 1000 health, or HP and 2 stamina points, or SP. Each attack uses SP from 0.5 to 2. You regain all SP at the end of your turn. Finishers can only be used once per player when they have 500 HP or less, and it uses 2 SP.")
time.sleep(3)
print("\nEffects: \nBurn: lose 50 HP at the end of your turn, lasts 3 turns\nPoison: lose 30 HP at the end of your turn, lasts 5 turns\nBleed: lose 10 HP every turn + 10 HP for every hit taken, lasts 10 turns or until healed\nSummon: at the end of your turn, lose 30 HP\n")
time.sleep(3)
print("\nWhen the battle starts, type the attack you want to use and hit enter to use it if posible, enter 'end' to end your turn when you are out of SP")
time.sleep(3)

#set up variables
HP1 = 1000 #player health
HP2 = 1000 #bot health
SP1 = 2 #player stamina
SP2 = 2 #bot stamina
burn1 = False #player is burned
burn2 = False #bot is burned
burnT1 = 0 #turns till burn is removed from player
burnT2 = 0 #turns till burn is removed from bot
poison1 = False #player is poisoned
poison2 = False #bot is poisoned
poisonT1 = 0 #turns till poison is removed from player
poisonT2 = 0 #turns till poison is removed from bot
bleed1 = False #player is bleeding
bleed2 = False #bot is bleeding
bleedT1 = 0 #turns till bleed is removed from player
bleedT2 = 0 #turns till bleed is removed from bot
summon1 = False #player is attacked by summon
summon2 = False #bot is attacked by summon
armor1 = False #player has armor ready
armor2 = False #bot has armor ready
barrier1 = False #player has barrier ready
barrier2 = False #bot has barrier ready
regen1 = False #player is regenerating
regen2 = False #bot is regenerating
regenT1 = 0 #turns till regen removed from player
regenT2 = 0 #turns till regen removed from bot
finisher1 = False #player has used their finisher
finisher2 = False #bot has used their finisher
time.sleep(0.5)

#set up lists
weapons = ["Sword", "Hammer", "Dagger", "Bow and Arrows", "Gauntlets"]
spells = ["Ignis", "Glacies", "Tempestas", "Venenum" "Vocare"]
shields = ["Armor", "Barrier"]
potions = ["Heal", "Regen", "Cure"]
finishers = ["Lethal Execution", "Magus Exponentia Inspiratione", "Steel-Fist Beatdown"]
moveset1 = ["weapon", "spell", "shield", "potion", "finisher"] #player's moveset 
moveset2 = ["weapon", "spell", "shield", "potion", "finisher"] #bot's moveset
time.sleep(0.5)

#player chooses moves
moveset1[0] = str(input("Select a Weapon: \nSword: deals 50 HP with 50% chance to inflict bleed, 1 SP\nHammer: 50% to deal 100 HP, 50% chance to do nothing, 1 SP\nDagger: deals 20 HP, 25% chance to bleed, 0.5 SP\nBow and Arrow: hits 1 to 5 times, each hit deals 20 HP, 1 SP\nGuantlets: deals 70 HP, 1 SP\n"))
time.sleep(0.5)
moveset1[1] = str(input("Select a Spell: \nIgnis: deals 30 HP, 50% chance to inflict burn, 1 SP\nGlacies: deals 30 HP, opponent loses 1/2 SP, 1 SP \nTempestas: hits 1 to 3 times, each hit deals 30 HP, 1 SP\nVenenum: deals 30 HP, 50% chance to inflict poison, 1 SP\nVocare: deals 30 HP, inflicts summon effect, 1 SP\n"))
time.sleep(0.5)
moveset1[2] = str(input("Select a Shield: \nArmor: next weapon attack deals 50 less HP\nBarrier: next spell attack deals 50 less HP\n"))
time.sleep(0.5)
moveset1[3] = str(input("Select a Potion: \nHeal: heal 100 HP\nRegen: for the next 3 turns, heal 50 HP\nCure: heal 50 HP and remove effects\n"))
time.sleep(0.5)
moveset1[4] = str(input("Select a Finisher: \nLethal Execution: deals 500 HP, inflicts bleed, 2 SP\nMagus Exponentia Inspiratione: hits 1-3 times, each hit deals 200 HP, inflicts burn and poison, opponent loses 1/2 SP, 2 SP\nSteel-Fist Beatdown: hits 1-10 times, each hit deals 100 HP, 2 SP\n"))
time.sleep(0.5)
print(moveset1)

#bot chooses moves
randomNum = random.randint(1,5)
moveset2[0] = weapons[randomNum-1]

randomNum = random.randint(1,5)
moveset2[1] = spells[randomNum-1]

randomNum = random.randint(1,2)
moveset2[2] = shields[randomNum-1]

randomNum = random.randint(1,3)
moveset2[3] = potions[randomNum-1]
    
randomNum = random.randint(1,3)
moveset2[4] = finishers[randomNum-1]


#start battle
while HP1 > 0 and HP2 > 0:
    time.sleep(1)
    print("Player's turn")
    armor1 = False #player has armor ready
    barrier1 = False #player has barrier ready
    while attack != end:
        attack = input("\nEnter attack:\n")
        if str(attack.capitalize()) == "Sword" and str(attack.capitalize()) == str(moveset1[0].capitalize()):
            if armor2 == False:
                HP2 -= 50
                print("CPU took 50 HP")
                if bleed2 == True:
                    HP2 -= 10
                    print("CPU's wounds deepened, -10 HP")
                randomNum = random.randint(1,2)
                if randomNum == 1 and bleed2 == False:
                    bleed2 = True
                    bleedT2 = 10
                    print("CPU is bleeding")
            else:
                print("CPU defended himself from the attack")
            SP1 -= 1
        elif str(attack.capitalize()) == "Hammer" and str(attack.capitalize()) == str(moveset1[0].capitalize()):
            if armor2 == False:
                randomNum = random.randint(1,2)
                if randomNum == 1:
                    HP2 -= 100
                    print("CPU took 100 HP")
                    if bleed2 == True:
                        HP2 -= 10
                        print("CPU's wounds deepened, -10 HP")
                else:
                    print("You missed")
            else:
                print("CPU defended himself from the attack")
            SP1 -= 1
        elif str(attack.capitalize()) == "Dagger" and str(attack.capitalize()) == str(moveset1[0].capitalize()):
            if armor2 == False:
                HP2 -= 20
                print("CPU took 20 HP")
                if bleed2 == True:
                    HP2 -= 10
                    print("CPU's wounds deepened, -10 HP")
                randomNum = random.randint(1,4)
                if randomNum == 1 and bleed2 == False:
                    bleed2 = True
                    bleedT2 = 10
                    print("CPU is bleeding")
            else:
                print("CPU defended himself from the attack")
            SP1 -= 0.5
        elif str(attack.capitalize()) == "Bow and Arrow" and str(attack.capitalize()) == str(moveset1[0].capitalize()):
            if armor2 == False:
                randomNum = random.randint(1,5)
                while randomNum > 0:
                    HP2 -= 20
                    print("CPU took 20 HP")
                    if bleed2 == True:
                        HP2 -= 10
                        print("CPU's wounds deepened, -10 HP")
                    randomNum -= 1
            else:
                print("CPU defended himself from the attack")
            SP1 -= 1
        elif str(attack.capitalize()) == "Gauntlets" and str(attack.capitalize()) == str(moveset1[0].capitalize()):
            if armor2 == False:
                HP2 -= 70
                print("CPU took 70 HP")
                if bleed2 == True:
                    HP2 -= 10
                    print("CPU's wounds deepened, -10 HP")
            else:
                print("CPU defended himself from the attack")
            SP1 -= 1
        elif str(attack.capitalize()) == "Ignis" and str(attack.capitalize()) == str(moveset1[1].capitalize()):
            if barrier2 == False:
                HP2 -= 30
                print("CPU took 30 HP")
                randomNum = random.randint(1,2)
                if randomNum == 1 and burn2 == False:
                    burn2 = True
                    burnT2 = 3
                    print("CPU got Burned")
            else:
                print("CPU defended himself from the attack")
            SP1 -= 1
        elif str(attack.capitalize()) == "Glacies" and str(attack.capitalize()) == str(moveset1[1].capitalize()):
            if barrier2 == False:
                HP2 -= 30
                print("CPU took 30 HP")
                SP2 -= 0.5
                print("CPU got Frozen")
            else:
                print("CPU defended himself from the attack")
            SP1 -= 1
        elif str(attack.capitalize()) == "Tempestas" and str(attack.capitalize()) == str(moveset1[1].capitalize()):
            if barrier2 == False:
                randomNum = random.randint(1,3)
                while randomNum > 0:
                    HP2 -= 30
                    print("CPU took 30 HP")
                    randomNum -= 1
            else:
                print("CPU defended himself from the attack")
            SP1 -= 1
        elif str(attack.capitalize()) == "Venenum" and str(attack.capitalize()) == str(moveset1[1].capitalize()):
            if barrier2 == False:
                HP2 -= 30
                print("CPU took 30 HP")
                randomNum = random.randint(1,2)
                if randomNum == 1 and poison2 == False:
                    poison2 = True
                    poisonT2 = 5
                    print("CPU got poisoned")
            else:
                print("CPU defended himself from the attack")
            SP1 -= 1
        elif str(attack.capitalize()) == "Vocare" and str(attack.capitalize()) == str(moveset1[1].capitalize()):
            if barrier2 == False:
                HP2 -= 30
                print("CPU took 30 HP")
                randomNum = random.randint(1,2)
                if randomNum == 1 and summon2 == False:
                    summon2 = True
                    print("Player summons a warrior to fight")
            else:
                print("CPU defended himself from the attack")
            SP1 -= 1
        elif str(attack.capitalize()) == "Armor" and str(attack.capitalize()) == str(moveset1[2].capitalize()):
            armor1 = True
            print("Player is defending himself against weapons")
            SP1 -= 1
        elif str(attack.capitalize()) == "Barrier" and str(attack.capitalize()) == str(moveset1[2].capitalize()):
            barrier1 = True
            print("Player is defending himself against spells")
            SP1 -= 1
        elif str(attack.capitalize()) == "Heal" and str(attack.capitalize()) == str(moveset1[3].capitalize()):
            HP1 += 100
            if bleed1 == True:
                bleed1 = False
                bleedT1 = 0
                print("Player's wounds heal")
            print("Player heals himself")
            SP1 -= 1
        elif str(attack.capitalize()) == "Regen" and str(attack.capitalize()) == str(moveset1[3].capitalize()):
            regen1 = True
            regenT1 = 3
            print("Player is regenerating")
            SP1 -= 1
        elif str(attack.capitalize()) == "Cure" and str(attack.capitalize()) == str(moveset1[3].capitalize()):
            HP1 += 50
            burn1 = False
            burnT1 = 0
            poison1 = False
            poisonT1 = 0
            if bleed1 == True:
                bleed1 = False
                bleedT1 = 0
                print("Player's wounds heal")
            print("Player cures himself")
            SP1 -= 1
        elif str(attack.capitalize()) == "Lethal Execution" and str(attack.capitalize()) == str(moveset1[4].capitalize()) and finisher1 == False and HP1 <= 500:
            HP2 -= 500
            print("CPU took 500 HP")
            if bleed2 == True:
                HP2 -= 10
                print("CPU's wounds deepened, -10 HP")
            if bleed2 == False:
                bleed2 = True
                bleedT2 = 10
                print("CPU is bleeding")
            SP1 -= 2
            finisher1 = True
        elif str(attack.capitalize()) == "Magus Exponentia Inspiratione" and str(attack.capitalize()) == str(moveset1[4].capitalize()) and finisher1 == False and HP1 <= 500:
            randomNum = random.randint(1,3)
            while randomNum > 0:
                HP2 -= 200
                print("CPU took 200 HP")
            burn2 = True
            burnT2 = 3
            poison2 = True
            poisonT2 = 5
            SP2 -= 0.5
            print("CPU got burned, poisoned, and frozen")
            SP1 -= 2
            finisher1 = True
        elif str(attack.capitalize()) == "Steel-Fist Beatdown" and str(attack.capitalize()) == str(moveset1[4].capitalize()) and finisher1 == False and HP1 <= 500:
            randomNum = random.randint(1,10)
            while randomNum > 0:
                HP2 -= 100
                print("CPU took 100 HP")
                if bleed2 == True:
                    HP2 -= 10
                    print("CPU's wounds deepened, -10 HP")
            SP1 -= 2
            finisher1 = True
        else:
            print("Either you don't have that move equipped, you haven't fulfilled the conditions for using  finisher, or you miss-spelled it. Please try again. ")
        time.sleep(1)
        print("\nPlayer HP: "+str(HP1)+"\nCPU HP: "+str(HP2)+"\nPlayer SP: "+str(SP1))
        #check for effects
    if bleed1 == True:
        HP1 -= 10
        bleedT1 -= 1
        print("Player is bleeding, -50 HP")
        if bleedT1 == 0:
            bleed1 = False
    if burn1 == True:
        HP1 -= 50
        burnT1 -= 1
        print("Player is burning, -50 HP")
        if burnT1 == 0:
            burn1 = False
    if poison1 == True:
        HP1 -= 30
        poisonT1 -= 1
        print("Player is poisoned, -30 HP")
        if poisonT1 == 0:
            poison1 = False
    if summon1 == True:
        HP1 -= 30
        print("Player was attacked by the summoned warrior, -30 HP")
        summon1 == False
    if regen1 == True:
        HP1 += 50
        regenT1 -= 1
        print("Player regenerated, +50 HP")
        if bleed1 == True:
            bleed1 = False
            bleedT1 = 0
            print("Player's wounds healed")
        if regenT1 == 0:
            regen1 = False
    SP1 = 2
    time.sleep(1)
    print("CPU's turn")
    armor2 = False #player has armor ready
    barrier2 = False #player has barrier ready
    while SP2 > 0.5:
        randomNum = random.randint(0,4)
        attack = moveset2[randomNum]
        if str(attack.capitalize()) == "Sword":
            if armor1 == False:
                HP1 -= 50
                print("Player took 50 HP")
                if bleed1 == True:
                    HP1 -= 10
                    print("Player's wounds deepened, -10 HP")
                randomNum = random.randint(1,2)
                if randomNum == 1 and bleed1 == False:
                    bleed1 = True
                    bleedT1 = 10
                    print("Player is bleeding")
            else:
                print("Player defended himself from the attack")
            SP2 -= 1
        elif str(attack.capitalize()) == "Hammer":
            if armor1 == False:
                randomNum = random.randint(1,2)
                if randomNum == 1:
                    HP1 -= 100
                    print("Player took 100 HP")
                    if bleed1 == True:
                        HP1 -= 10
                        print("Player's wounds deepened, -10 HP")
                else:
                    print("CPU missed")
            else:
                print("Player defended himself from the attack")
            SP2 -= 1
        elif str(attack.capitalize()) == "Dagger":
            if armor1 == False:
                HP1 -= 20
                print("Player took 20 HP")
                if bleed1 == True:
                    HP1 -= 10
                    print("Player's wounds deepened, -10 HP")
                randomNum = random.randint(1,4)
                if randomNum == 1 and bleed1 == False:
                    bleed1 = True
                    bleedT1 = 10
                    print("Player is bleeding")
            else:
                print("Player defended himself from the attack")
            SP2 -= 0.5
        elif str(attack.capitalize()) == "Bow and Arrow":
            if armor1 == False:
                randomNum = random.randint(1,5)
                while randomNum > 0:
                    HP1 -= 20
                    print("Player took 20 HP")
                    if bleed1 == True:
                        HP1 -= 10
                        print("Player's wounds deepened, -10 HP")
                    randomNum -= 1
            else:
                print("Player defended himself from the attack")
            SP2 -= 1
        elif str(attack.capitalize()) == "Gauntlets":
            if armor1 == False:
                HP1 -= 70
                print("Player took 70 HP")
                if bleed1 == True:
                    HP1 -= 10
                    print("Player's wounds deepened, -10 HP")
            else:
                print("Player defended himself from the attack")
            SP2 -= 1
        elif str(attack.capitalize()) == "Ignis":
            if barrier1 == False:
                HP1 -= 30
                print("Player took 30 HP")
                randomNum = random.randint(1,2)
                if randomNum == 1 and burn1 == False:
                    burn1 = True
                    burnT = 3
                    print("Player got Burned")
            else:
                print("Player defended himself from the attack")
            SP2 -= 1
        elif str(attack.capitalize()) == "Glacies":
            if barrier1 == False:
                HP1 -= 30
                print("Player took 30 HP")
                SP1 -= 0.5
                print("Player got Frozen")
            else:
                print("Player defended himself from the attack")
            SP2 -= 1
        elif str(attack.capitalize()) == "Tempestas":
            if barrier1 == False:
                randomNum = random.randint(1,3)
                while randomNum > 0:
                    HP1 -= 30
                    print("Player took 30 HP")
                    randomNum -= 1
            else:
                print("Player defended himself from the attack")
            SP2 -= 1
        elif str(attack.capitalize()) == "Venenum":
            if barrier1 == False:
                HP1 -= 30
                print("Player took 30 HP")
                randomNum = random.randint(1,2)
                if randomNum == 1 and poison1 == False:
                    poison1 = True
                    poisonT1 = 5
                    print("Player got poisoned")
            else:
                print("Player defended himself from the attack")
            SP2 -= 1
        elif str(attack.capitalize()) == "Vocare":
            if barrier1 == False:
                HP1 -= 30
                print("Player took 30 HP")
                randomNum = random.randint(1,2)
                if randomNum == 1 and summon1 == False:
                    summon1 = True
                    print("CPU summons a warrior to fight")
            else:
                print("Player defended himself from the attack")
            SP2 -= 1
        elif str(attack.capitalize()) == "Armor":
            armor2 = True
            print("CPU is defending himself against weapons")
            SP2 -= 1
        elif str(attack.capitalize()) == "Barrier":
            barrier2 = True
            print("CPU is defending himself against spells")
            SP2 -= 1
        elif str(attack.capitalize()) == "Heal":
            HP2 += 100
            if bleed2 == True:
                bleed2 = False
                bleedT2 = 0
                print("CPU's wounds heal")
            print("CPU heals himself")
            SP2 -= 1
        elif str(attack.capitalize()) == "Regen":
            regen2 = True
            regenT2 = 3
            print("CPU is regenerating")
            SP2 -= 1
        elif str(attack.capitalize()) == "Cure":
            HP2 += 50
            burn2 = False
            burnT2 = 0
            poison2 = False
            poisonT2 = 0
            if bleed2 == True:
                bleed2 = False
                bleedT2 = 0
                print("CPU's wounds heal")
            print("CPU cures himself")
            SP2 -= 1
        elif str(attack.capitalize()) == "Lethal Execution" and finisher2 == False and HP2 <= 500:
            HP1 -= 500
            print("Player took 500 HP")
            if bleed1 == True:
                HP1 -= 10
                print("Player's wounds deepened, -10 HP")
            if bleed1 == False:
                bleed1 = True
                bleedT1 = 10
                print("Player is bleeding")
            SP2 -= 2
            finisher2 = True
        elif str(attack.capitalize()) == "Magus Exponentia Inspiratione" and finisher2 == False and HP1 <= 500:
            randomNum = random.randint(1,3)
            while randomNum > 0:
                HP1 -= 200
                print("Player took 200 HP")
            burn1 = True
            burnT1 = 3
            poison1 = True
            poisonT1 = 5
            SP1 -= 0.5
            print("Player got burned, poisoned, and frozen")
            SP2 -= 2
            finisher2 = True
        elif str(attack.capitalize()) == "Steel-Fist Beatdown" and finisher2 == False and HP1 <= 500:
            randomNum = random.randint(1,10)
            while randomNum > 0:
                HP1 -= 100
                print("Player took 100 HP")
                if bleed1 == True:
                    HP1 -= 10
                    print("Player's wounds deepened, -10 HP")
                randomNum -= 1
            SP2 -= 2
            finisher1 = True
        else:
            print("CPU made a mistake!?!?! Fix ASAP")
        time.sleep(1)
        print("\nPlayer HP: "+str(HP1)+"\nCPU HP: "+str(HP2)+"\nCPU SP: "+str(SP2))
        
        #check for effects
    if bleed2 == True:
        HP2 -= 10
        bleedT2 -= 1
        print("CPU is bleeding, -50 HP")
        if bleedT2 == 0:
            bleed2 = False
    if burn2 == True:
        HP2 -= 50
        burnT2 -= 1
        print("CPU is burning, -50 HP")
        if burnT2 == 0:
            burn2 = False
    if poison2 == True:
        HP2 -= 30
        poisonT2 -= 1
        print("CPU is poisoned, -30 HP")
        if poisonT2 == 0:
            poison2 = False
    if summon2 == True:
        HP2 -= 30
        print("CPU was attacked by the summoned warrior, -30 HP")
        summon2 == False
    if regen2 == True:
        HP2 += 50
        regenT2 -= 1
        print("CPU regenerated, +50 HP")
        if bleed2 == True:
            bleed1 = False
            bleedT2 = 0
            print("CPU's wounds healed")
        if regenT2 == 0:
            regen2 = False
    SP2 = 2
#end battle and results
if HP1 > 0:
    print("\nYou win!\nCPU lost!")
elif HP2 > 0:
    print("\nCPU wins!\n You lose!")




