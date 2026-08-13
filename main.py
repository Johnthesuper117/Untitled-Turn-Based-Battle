import os
import json
import random
from collections import deque
from time import sleep

def lineBreak(x):
    try:
        screen_width = os.get_terminal_size().columns
    except OSError:
        screen_width = 80
    print("\n" + "-" * screen_width + "\n")
    sleep(x)

def rules(x):
    print("Hello and Welcome to Untitled Turn-Based Battle version Alpha")
    lineBreak(x)
    print("How to play:\nFirst, before the battle starts, you select one attack for each category: Weapon, Spell, Shield, Potion, and Finisher. \nDuring the battle, you get to choose your attacks until you run out of stamina points. Then, your opponent does the same. This continues until one of the players lose all of their health, the one who remains is the winner!")
    lineBreak(x)
    print("Rules: Both players have 1000 health (HP) and 2 stamina points (SP). Each attack uses SP from 0.5 to 2. You regain all SP at the end of your turn. Finishers can only be used once per player when they have 500 HP or less, and it uses 2 SP.")
    lineBreak(x)
    print("Effects: \nBurn: lose 50 HP at the end of your turn, lasts 3 turns\nPoison: lose 30 HP at the end of your turn, lasts 5 turns\nBleed: lose 10 HP every turn, lasts 10 turns or until healed\nSummon: at the end of your turn, lose 100 HP\n")
    lineBreak(x)
    print("When the battle starts, type the attack you want to use and hit enter to use it if possible. Enter 'END' to end your turn when you are out of SP.")
    lineBreak(x)

def load_config():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: The configuration file is empty or contains invalid JSON.")
        return {}
    except FileNotFoundError:
        print("Error: Configuration file not found. Make sure config.json exists!")
        return {}

# Dictionary mapping effect names to their stats based on your rules
EFFECT_STATS = {
    "Burn": {"healthchange": -50, "turns": 3},
    "Poison": {"healthchange": -30, "turns": 5},
    "Bleed": {"healthchange": -10, "turns": 10},
    "Summon": {"healthchange": -100, "turns": 1},
    "Freeze": {"healthchange": 0, "turns": 2}, 
    "Regen": {"healthchange": 25, "turns": 5}, 
    "Heal": {"healthchange": 200, "turns": 1}
}

class Effect:
    def __init__(self, name, healthchange, turns):
        self.name = name
        self.healthchange = healthchange
        self.turns = turns

class Action:
    def __init__(self, name, action_type, damage, sp, effect=None, effect_chance=0):
        self.name = name
        self.type = action_type
        self.damage = damage
        self.sp = sp
        self.effect = effect
        self.effect_chance = effect_chance

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 1000
        self.sp = 2.0
        self.effects = deque()
        self.moveset = []
        self.used_finisher = False

    def apply_effects(self):
        for effect in list(self.effects):
            self.hp += effect.healthchange
            print(f"{self.name} took {abs(effect.healthchange)} damage from {effect.name}! (HP: {self.hp})")
            effect.turns -= 1
            if effect.turns <= 0:
                print(f"{self.name}'s {effect.name} wore off.")
                self.effects.remove(effect)

    def add_effect(self, effect):
        new_effect = Effect(effect.name, effect.healthchange, effect.turns)
        self.effects.append(new_effect)

class Game:
    def __init__(self, config):
        self.config = config
        self.player = None
        self.cpu = None
        self.moves = self.load_moves()

    def load_moves(self):
        moves = {}
        for category in ["weapons", "spells", "shields", "potions", "finishers"]:
            if category not in self.config:
                continue
            for item in self.config[category]:
                effect_name = item.get("effect")
                effect = None
                if effect_name and effect_name in EFFECT_STATS:
                    stats = EFFECT_STATS[effect_name]
                    effect = Effect(effect_name, stats["healthchange"], stats["turns"])
                
                moves[item["name"].upper()] = Action(
                    item["name"], 
                    category, 
                    item.get("damage", 0), 
                    item.get("stamina_cost", 1.0), 
                    effect, 
                    item.get("effect_chance", 0)
                )
        return moves

    def setup_players(self):
        self.player = Player(input("Enter your username: "))
        self.cpu = Player("CPU")
        self.setup_moveset(self.player, "player")
        self.setup_moveset(self.cpu, "cpu")

    def setup_moveset(self, player, player_type):
        print(f"\nSetting up {player.name}'s moveset...")
        for category in ["weapons", "spells", "shields", "potions", "finishers"]:
            if category not in self.config:
                continue
            options = [item["name"] for item in self.config[category]]
            if player_type == "player":
                print(f"\n--- Choose your {category.upper()} ---")
                chosen_move = self.select_move(options)
                player.moveset.append(chosen_move.upper())
            else:
                player.moveset.append(random.choice(options).upper())
        print(f"\n{player.name}'s equipped moves: {', '.join(player.moveset)}")

    def select_move(self, options):
        while True:
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            try:
                choice = int(input("> ")) - 1
                if 0 <= choice < len(options):
                    return options[choice]
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def player_turn(self):
        self.player.sp = 2.0 
        print(f"\n=== {self.player.name}'s Turn ===")
        
        while self.player.sp > 0:
            print(f"\nHP: {self.player.hp}/1000 | SP: {self.player.sp}/2.0")
            print(f"Available moves: {', '.join(self.player.moveset)}")
            move_name = input("Enter your move (or 'END' to finish turn): ").upper()
            
            if move_name == "END":
                break
                
            if move_name in self.player.moveset:
                move = self.moves[move_name]
                success = self.perform_attack(self.player, self.cpu, move)
                if self.check_game_over():
                    return
            else:
                print("Invalid move or move not equipped!")
                
        self.player.apply_effects()
        lineBreak(1)

    def cpu_turn(self):
        self.cpu.sp = 2.0
        print(f"\n=== CPU's Turn ===")
        print(f"CPU HP: {self.cpu.hp}/1000")
        
        while self.cpu.sp > 0:
            valid_moves = []
            for m_name in self.cpu.moveset:
                m = self.moves[m_name]
                if m.sp <= self.cpu.sp:
                    if m.type == "finishers" and (self.cpu.hp > 500 or self.cpu.used_finisher):
                        continue
                    valid_moves.append(m_name)
                    
            if not valid_moves:
                break 
                
            move_name = random.choice(valid_moves)
            move = self.moves[move_name]
            self.perform_attack(self.cpu, self.player, move)
            sleep(1)
            
            if self.check_game_over():
                return
                
        self.cpu.apply_effects()
        lineBreak(1)

    def perform_attack(self, attacker, defender, move):
        # Finisher Checks
        if move.type == "finishers":
            if attacker.hp > 500:
                print(f"{attacker.name} cannot use a Finisher until HP is 500 or below!")
                return False
            if attacker.used_finisher:
                print(f"{attacker.name} has already used their Finisher this battle!")
                return False

        if move.sp > attacker.sp:
            print(f"{attacker.name} does not have enough SP to use {move.name}! (Costs {move.sp})")
            return False
        
        attacker.sp -= move.sp
        
        if move.type in ["potion", "potions", "shield", "shields"]:
            target = attacker 
            print(f"> {attacker.name} used {move.name}!")
        else:
            defender.hp -= move.damage
            target = defender
            print(f"> {attacker.name} used {move.name} and dealt {move.damage} damage to {defender.name}!")
        
        if move.type == "finisher" or move.type == "finishers":
            attacker.used_finisher = True
            
        if move.effect and random.randint(1, 100) <= move.effect_chance:
            target.add_effect(move.effect)
            print(f"> {target.name} is now affected by {move.effect.name}!")
            
        return True

    def check_game_over(self):
        if self.player.hp <= 0 and self.cpu.hp <= 0:
            print("\nIt's a draw!")
            return True
        elif self.player.hp <= 0:
            print(f"\n{self.cpu.name} wins! You lost!")
            return True
        elif self.cpu.hp <= 0:
            print(f"\n{self.player.name} wins! You defeated the CPU!")
            return True
        return False

    def play(self):
        print("Starting the game!")
        lineBreak(1)
        rules(1)
        self.setup_players()
        
        while True:
            self.player_turn()
            if self.check_game_over():
                break
            self.cpu_turn()
            if self.check_game_over():
                break

if __name__ == "__main__":
    config_data = load_config()
    if config_data:
        game_instance = Game(config_data)
        game_instance.play()
