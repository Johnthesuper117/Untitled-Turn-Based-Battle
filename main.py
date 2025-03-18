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
print("\nEffects: \nBurn: lose 50 HP at the end of your turn, lasts 3 turns\nPoison: lose 30 HP at the end of your turn, lasts 5 turns\nBleed: lose 10 HP every turn + 10 HP for every hit taken, lasts 10 turns or until healed\nSummon: at the end of your turn, lose 100 HP\n")
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

class Player:
    def __init__(self, name:str, weapon:str, spell:str, shield:str, potion:str, finisher:str):
        self.name = name
        self.hp = 1000
        self.defence = 0
        self.sp = 2.0
        self.bleed = Effect("Bleed", 0, 0)
        self.burn = Effect("Burn", 0, 0)
        self.poison = Effect("Poison", 0, 0)
        self.summon = Effect("Summon", 0, 0)
        self.armor = False
        self.barrier = False
        self.regen = Effect("Regen", 0, 0)
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
            chance = random.randint(0, self.effectchance)
            self.effect = effect

#set up lists
weapons = config["weapons"]
spells = config["spells"]
shields = config["shields"]
potions = config["potions"]
finishers = config["finishers"]


#set up moves
Sword = Action("", "weapon", 0, 50, 1, 50, "Bleed")

#player chooses moves
player = Player(input("Enter Username:\n"), 'weapon', 'spell', 'shield', 'potion', 'finisher')

player.moveset[0] = str(input(f"Select a Weapon: \nSword(1): deals 50 HP with 50% chance to inflict bleed, 1 SP\nHammer(2): 50% to deal 100 HP, 50% chance to do nothing, 1 SP\nDagger(3): deals 20 HP, 25% chance to bleed, 0.5 SP\nBow and Arrow(4): hits 1 to 5 times, each hit deals 20 HP, 1 SP\nGuantlets(5): deals 70 HP, 1 SP\n"))
sleep(0.5)
if player.moveset[0] != weapons[0] or player.moveset[1] != weapons[1] or player.moveset[2] != weapons[2] or player.moveset[3] != weapons[3] or player.moveset[4] != weapons[4]:
    player.moveset = weapons[player.moveset]

player.moveset[1] = str(input(f"Select a Spell: \nIgnis(1): deals 30 HP, 50% chance to inflict burn, 1 SP\nGlacies(2): deals 30 HP, opponent loses 1/2 SP, 1 SP \nTempestas(3): hits 1 to 3 times, each hit deals 30 HP, 1 SP\nVenenum(4): deals 30 HP, 50% chance to inflict poison, 1 SP\nVocare(5): deals 30 HP, inflicts summon effect, 1 SP\n"))
sleep(0.5)
if player.moveset[0] != spells[0] or player.moveset[1] != spells[1] or player.moveset[2] != spells[2] or player.moveset[3] != spells[3] or player.moveset[4] != spells[4]:
    player.moveset = spells[player.moveset]

player.moveset[2] = str(input(f"Select a Shield: \nArmor(1): next weapon attack deals 50 less HP\nBarrier(2): next spell attack deals 50 less HP\n"))
sleep(0.5)
if player.moveset[0] != shields[0] or player.moveset[1] != shields[1] or player.moveset[2] != shields[2] or player.moveset[3] != shields[3] or player.moveset[4] != shields[4]:
    player.moveset = shields[player.moveset]

player.moveset[3] = str(input(f"Select a Potion: \nHeal(1): heal 100 HP\nRegen(2): for the next 3 turns, heal 50 HP\nCure(3): heal 50 HP and remove effects\n"))
sleep(0.5)
if player.moveset[0] != potions[0] or player.moveset[1] != potions[1] or player.moveset[2] != potions[2] or player.moveset[3] != potions[3] or player.moveset[4] != potions[4]:
    player.moveset = potions[player.moveset]

player.moveset[4] = str(input(f"Select a Finisher: \nLethal Execution(1): deals 500 HP, inflicts bleed, 2 SP\nMagus Exponentia Inspiratione(2): hits 1-3 times, each hit deals 200 HP, inflicts burn and poison, opponent loses 1/2 SP, 2 SP\nSteel-Fist Beatdown(3): hits 1-10 times, each hit deals 100 HP, 2 SP\n"))
sleep(0.5)
if player.moveset[0] != finishers[0] or player.moveset[1] != finishers[1] or player.moveset[2] != finishers[2] or player.moveset[3] != finishers[3] or player.moveset[4] != finishers[4]:
    player.moveset = finishers[player.moveset]
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

#set up functions
def Attack(turn, type, damage, effect):
    if turn == "PLAYER":
        damage -= cpu.defence
        cpu.defence = 0
        print(f"{player.name} Broke CPU's Defences")
        if damage <= 0:
            pass
        if cpu.bleed.turns > 0:
            damage += 10
            print("CPU's wounds deepen")
        cpu.hp -= damage
        print(f"CPU took {damage}")
        if effect.upper() == "BLEED":
            cpu.bleed == Effect("Bleed", -10, 10)
            print("CPU is bleeding")

run = True #flag that keeps the game running
myturn = True #flag that tracks turn
while run and player.hp > 0 and cpu.hp > 0:
    
    while myturn:
        print("Player's turn")
        #my turn here
            #ask for which attack to do &verify
            #perform the attack (print damage done, effects, and update the target)
        #conditions to end turn: skip the rest of your turn or run out of stamina
        attack = input("\nEnter attack:\n").upper()
        print(attack)
        if attack[0] != player.moveset[0] or player.moveset[1] != player.moveset[1] or player.moveset[2] != player.moveset[2] or player.moveset[3] != player.moveset[3] or player.moveset[4] != player.moveset[4]:
            attack = player.moveset[player.moveset]
        if attack == player.moveset[0] or attack == player.moveset[1] or attack == player.moveset[2] or attack == player.moveset[3] or attack == player.moveset[4]:
            print(attack)
            if attack == "SWORD":
                Attack("PLAYER", Sword.type, Sword.damage, Sword.effect)
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

if cpu.hp <=0:
    print("Computer died!")
