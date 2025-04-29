# Untitled-Turn-Based-Battle (W.I.P.)

Untitled-Turn-Based-Battle, or UTBB, is a game where you make a moveset out of a list of options, and then you fight your opponent using said moveset. Currently a work in progress

How to play:

First, before the battle starts, you select one attack for each category: Weapon, Spell, Shield, Potion, and Finisher. 
During the battle, you get to choose your attacks until you run out of stamina points. Then, your opponent does the same. This continues until one of the players lose all of their health, the one who remains is the winner!

Rules: Both players have 1000 health, or HP and 2 stamina points, or SP. Each attack uses SP from 0.5 to 2. You regain all SP at the end of your turn. Finishers can only be used once per player when they have 500 HP or less, and it uses 2 SP.

Moves:

 - Sword = Action("", "weapon", 0, 50, 1, 50, "Bleed")
 - Hammer = Action("", "weapon", 0, 100, 1, 50, "hit")
 - Dagger = Action("", "weapon", 0, 50, 1, 100, "")
 - BowandArrow = Action("", "weapon", 0, 20, 1, 20, "multiHit")
 - Guantlets = Action("", "weapon", 0, 80, 1, 100, "")
 - Ignis = Action("", "spell", 0, 30, 1, 50, "Burn")
 - Glacies = Action("", "spell", 0, 30, 1, 50, "Freeze")
 - Tempestas = Action("", "spell", 0, 30, 1, 50, "multiHit")
 - Venenum = Action("", "spell", 0, 30, 1, 50, "Posion")
 - Vocare = Action("", "spell", 0, 30, 1, 50, "Summon")
 - Armor = Action("", "shield", 0, 0, 1, 0, "Armor")
 - Barrier = Action("", "shield", 0, 0, 1, 0, "Barrier")
 - Heal = Action("", "potion", 100, 0, 1, 100, "")
 - Regen = Action("", "potion", 50, 0, 1, 100, "Regen")
 - Cure = Action("", "potion", 100, 0, 1, 100, "Cure")
 - LethalExecution = Action("", "finisher", 0, 500, 2, 100, "Bleed")
 - MagusExponentiaInspiratione = Action("", "finisher", 0, 500, 2, 100, "All")
 - SteelFistBeatdown = Action("", "finisher", 0, 500, 2, 100, "")

Effects: 

 - Bleed: lose 10 HP every turn + 10 HP for every hit taken, lasts 10 turns or until healed

 - Burn: lose 50 HP at the end of your turn, lasts 3 turns

 - Freeze: lose 1 SP for your next turn, last 1 turn

 - Poison: lose 30 HP at the end of your turn, lasts 5 turns

 - Summon: at the end of your turn, lose 100 HP

When the battle starts, type the attack you want to use and hit enter to use it if posible, enter 'end' to end your turn when you are out of SP
