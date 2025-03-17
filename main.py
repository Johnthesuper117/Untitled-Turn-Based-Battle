#debug game and make sure every move works as intended, send to uncle Tim and David to test and give feedback, afterwards add finishing touches and last wave of testing, then release as finished version

#import stuff
import random, json
from time import sleep

with open('config.json') as config_file:
    config = json.load(config_file)

#intro, rules, and how to play
print("Hello and Welcome to Untitled Turn-Based Battle version Alpha")
sleep(1)
print("\nHow to play:\nFirst, before the battle starts, you select one attack for each category: Weapon, Spell, Shield, Potion, and Finisher. \nDuring the battle, you get to choose your attacks until you run out of stamina points. Then, your opponent does the same. This continues until one of the players lose all of their health, the one who remains is the winner!")
sleep(3)
print("\nRules: Both players have 1000 health, or HP and 2 stamina points, or SP. Each attack uses SP from 0.5 to 2. You regain all SP at the end of your turn. Finishers can only be used once per player when they have 500 HP or less, and it uses 2 SP.")
sleep(3)
print("\nEffects: \nBurn: lose 50 HP at the end of your turn, lasts 3 turns\nPoison: lose 30 HP at the end of your turn, lasts 5 turns\nBleed: lose 10 HP every turn + 10 HP for every hit taken, lasts 10 turns or until healed\nSummon: at the end of your turn, lose 30 HP\n")
sleep(3)
print("\nWhen the battle starts, type the attack you want to use and hit enter to use it if posible, enter 'end' to end your turn when you are out of SP")
sleep(3)


#set up variables
class Effect:
    def __init__(self, name:str, healthchange:int, turns:int):
        self.name = name
        self.active = False
        self.turns = turns
        self.healthchange = healthchange
        pass

Bleed = Effect("Bleed", -10, 10)
Burn = Effect("Burn", -50, 3)
Poison = Effect("Poison", -30, 5)
Regen = Effect("Regen", , )
Summon = Effect("Summon", -100, 1)


class Player:
    def __init__(self, name:str, weapon:str, spell:str, shield:str, potion:str, finisher:str):
        self.name = name
        self.hp = 1000
        self.sp = 2
        self.bleed = Bleed()
        self.burn = Burn()
        self.poison = Poison()
        self.summon = Summon()
        self.armor = False
        self.barrier = False
        self.regen = Effect("regen", "0", "0")
        self.finisher = False
        self.moveset = [weapon, spell, shield, potion, finisher]

class Action:
    def __init__(self, target, type, heal, damage, sp, effectchance, effect = ""):
        self.target = target
        self.type = type #physical weapon attack, magic attack, healing, finisher, armor
        self.heal = heal
        self.damage = damage
        self.stamina_cost = sp
        self.effectchance = effectchance
        if effect: 
            self.effect = Effect(effect)
            self.effectchance = effectchance




sleep(0.5)

#set up lists
weapons = config["weapons"]
spells = config["spells"]
shields = config["shields"]
potions = config["potions"]
finishers = config["finishers"]
sleep(0.5)

#set up moves

print(weapons)

#player chooses moves
#
player = Player(input("Enter Username:\n"), 'weapon', 'spell', 'shield', 'potion', 'finisher')

player.moveset[0] = str(input("Select a Weapon: \nSword: deals 50 HP with 50% chance to inflict bleed, 1 SP\nHammer: 50% to deal 100 HP, 50% chance to do nothing, 1 SP\nDagger: deals 20 HP, 25% chance to bleed, 0.5 SP\nBow and Arrow: hits 1 to 5 times, each hit deals 20 HP, 1 SP\nGuantlets: deals 70 HP, 1 SP\n"))
sleep(0.5)
player.moveset[1] = str(input("Select a Spell: \nIgnis: deals 30 HP, 50% chance to inflict burn, 1 SP\nGlacies: deals 30 HP, opponent loses 1/2 SP, 1 SP \nTempestas: hits 1 to 3 times, each hit deals 30 HP, 1 SP\nVenenum: deals 30 HP, 50% chance to inflict poison, 1 SP\nVocare: deals 30 HP, inflicts summon effect, 1 SP\n"))
sleep(0.5)
player.moveset[2] = str(input("Select a Shield: \nArmor: next weapon attack deals 50 less HP\nBarrier: next spell attack deals 50 less HP\n"))
sleep(0.5)
player.moveset[3] = str(input("Select a Potion: \nHeal: heal 100 HP\nRegen: for the next 3 turns, heal 50 HP\nCure: heal 50 HP and remove effects\n"))
sleep(0.5)
player.moveset[4] = str(input("Select a Finisher: \nLethal Execution: deals 500 HP, inflicts bleed, 2 SP\nMagus Exponentia Inspiratione: hits 1-3 times, each hit deals 200 HP, inflicts burn and poison, opponent loses 1/2 SP, 2 SP\nSteel-Fist Beatdown: hits 1-10 times, each hit deals 100 HP, 2 SP\n"))
sleep(0.5)
print(player.moveset)

#bot chooses moves

cpu = Player("CPU", 'weapon', 'spell', 'shield', 'potion', 'finisher')

randomNum = random.randint(1,5)
cpu.moveset[0] = weapons[randomNum-1]

randomNum = random.randint(1,5)
cpu.moveset[1] = spells[randomNum-1]

randomNum = random.randint(1,2)
cpu.moveset[2] = shields[randomNum-1]

randomNum = random.randint(1,3)
cpu.moveset[3] = potions[randomNum-1]
    
randomNum = random.randint(1,3)
cpu.moveset[4] = finishers[randomNum-1]


run = True #flag that keeps the game running
myturn = True #flag that tracks turn
while run and player.hp > 0 and cpu.hp > 0:
    
    while myturn:
        #my turn here
            #ask for which attack to do &verify
            #perform the attack (print damage done, effects, and update the target)
        #conditions to end turn: skip the rest of your turn or run out of stamina
        attack = input("\nEnter attack:\n")
        if attack.upper() == player.moveset[0] or attack.upper() == player.moveset[1] or attack.upper() == player.moveset[2] or attack.upper() == player.moveset[3] or attack.upper() == player.moveset[4]:
            print(attack.upper())
            player.hp += attack.upper.heal
            computer.hp -= attack.upper.hurt
        elif attack.upper() == 'END' or player.sp == 0:
            myturn = False
            print("End of Player's Turn")
    
    while not myturn:
        #computer turn here
        print("CPU's turn")
        
        #conditions to end turn: skip the rest of your turn or run out of stamina
        myturn = True
    
#print gameover: 
if player.hp <= 0:
    print("Player died!")

if computer.hp <=0:
    print("Computer died!")
