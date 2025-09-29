# Untitled-Turn-Based-Battle (W.I.P.)

Untitled-Turn-Based-Battle, or UTBB, is a game where you make a moveset out of a list of options, and then you fight your opponent using said moveset. Currently a work in progress

How to play:

First, before the battle starts, you select one attack for each category: Weapon, Spell, Shield, Potion, and Finisher. 
During the battle, you get to choose your attacks until you run out of stamina points. Then, your opponent does the same. This continues until one of the players lose all of their health, the one who remains is the winner!

Rules: Both players have 1000 health, or HP and 2 stamina points, or SP. Each attack uses SP from 0.5 to 2. You regain all SP at the end of your turn. Finishers can only be used once per player when they have 500 HP or less, and it uses 2 SP.

Moves:

 - Weapons
     - SWORD
         - Damage: 50
         - Effect: Bleed
         - Stamina Cost": 1
         - Effect Chance: 50

     - HAMMER
         - Damage: 100
         - Effect: hit
         - Stamina Cost": 1
         - Effect Chance": 50

     - DAGGER",
         - damage": 50,
         - effect": null,
         - stamina_cost": 0.5,
         - effect_chance": 100

     - BOW AND ARROW",
         - damage": 50,
         - effect": "multiHit",
         - stamina_cost": 1,
         - effect_chance": 20
    
       - GAUNTLETS",
         - damage": 80,
         - effect": "hit",
         - stamina_cost": 1,
         - effect_chance": 100

 - Spells": 

      - IGNIS",
         - damage": 50,
         - effect": "Burn",
         - stamina_cost": 1,
         - effect_chance": 50
         
     - GLACIES",
         - damage": 50,
         - effect": "Freeze",
         - stamina_cost": 1,
         - effect_chance": 50
   
     - TEMPESTAS",
         - damage": 50,
         - effect": "multiHit",
         - stamina_cost": 1,
         - effect_chance": 33

     - VENENUM",
         - damage": 50,
         - effect": "Poison",
         - stamina_cost": 1,
         - effect_chance": 50

     - VOCARE",
         - damage": 50,
         - effect": "Summon",
         - stamina_cost": 1,
         - effect_chance": 50

 - Shields":

     - ARMOR",
         - damage": 0,
         - effect": "",
         - stamina_cost": 1,
         - effect_chance": 50

     - BARRIER",
         - damage": 0,
         - effect": "",
         - stamina_cost": 1,
         - effect_chance": 50

 - potions":

      - HEAL",
         - damage": 0,
         - effect": "Heal",
         - stamina_cost": 1,
         - effect_chance": 50

     - REGEN",
         - damage": 0,
         - effect": "Regen",
         - stamina_cost": 1,
         - effect_chance": 50

     - CURE",
         - damage": 0,
         - effect": "Cure",
         - stamina_cost": 1,
         - effect_chance": 50

 - finishers": 

     - LETHAL EXECUTION",
         - damage": 500,
         - effect": "Bleed",
         - stamina_cost": 2,
         - effect_chance": 100

     - MAGUS EXPONENTIA INSPIRATIONE",
         - Damage": 300,
         - Effect": "All",
         - Stamina_cost": 2,
         - Effect_chance": 33

     - STEEL-FIST BEATDOWN
         - Damage: 100
         - effect: "multiHit
         - Stamina Cost: 2
         - Effect Chance: 10



Effects: 

 - Bleed: lose 10 HP every turn + 10 HP for every hit taken, lasts 10 turns or until healed

 - Burn: lose 50 HP at the end of your turn, lasts 3 turns

 - Freeze: lose 1 SP for your next turn, last 1 turn

 - Poison: lose 30 HP at the end of your turn, lasts 5 turns

 - Summon: at the end of your turn, lose 100 HP


When the battle starts, type the attack you want to use and hit enter to use it if posible, enter 'end' to end your turn when you are out of SP
