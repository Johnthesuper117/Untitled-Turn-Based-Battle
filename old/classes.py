import time, random

#weapon class with subclasses
#player class
class Effect:
    def __init__(self, name:str, damage:int, turns:int=0):
        self.name = name
        self.active = False
        self.turns = turns
        self.damage = damage
        pass

#practice instances of effects: 
#burn = Effect("burn", 50, 3)
#poison = Effect("poison", 30, 5)
#bleed = Effect("bleed", 10, 10)
#**make sure +10dmg to hits, cureable


#Intro here



class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 1000
        self.sp = 2
        self.burn = Effect("burn")
        self.bleed = Effect("bleed")
        self.poison = Effect("poison")
        self.summon = False
        self.armor = False
        self.barrier = False
        self.regen = Effect('regen')
        self.finisher = False

#

class Action:
    def __init__(self, target, type, damage, sp, effect = ""):
        self.target = target
        self.type = type #physical weapon attack, magic attack, healing, finisher, armor
        self.damage:int = damage
        self.stamina_cost = sp
        if effect: 
            self.effect = Effect(effect)



#instances of classes
player = Player('player') #instance of the player class for human player
computer = Player('computer') #instance of the player class for computer player

#practice instances of weapons below: 
sword = Action("other", "weapon", 50, 1, 'bleed')
sword.effectchance = 50
hammer = Action()
hammer.damagechance = 50
dagger = Action()
dagger.effectchance = 25
bow = Action()
bow.hits = [1,2,3,4,5]
gauntlets = Action()
#magic attacks:
ignis= Action()
ignis.effectchance = 50
glacies = Action()
glacies.sp_damage = 1


#ASK WHICH ACTION FUNCTION


#PERFORM AN ACTION FUNCTION


#game loop: 
run = True #flag that keeps the game running
myturn = True #flag that tracks turn
while run and player.hp > 0 and computer.hp > 0:
    
    while myturn:
        #my turn here
            #ask for which attack to do &verify
            #perform the attack (print damage done, effects, and update the target)
        #conditions to end turn: skip the rest of your turn or run out of stamina
        myturn = False
    
    while not myturn:
        #computer turn here

        #conditions to end turn: skip the rest of your turn or run out of stamina
        myturn = True
    
#print gameover: 
if player.hp <= 0:
    print("Player died!")

if computer.hp <=0:
    print("computer died!")

