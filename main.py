#debug game and make sure every move works as intended, send to uncle Tim and David to test and give feedback, afterwards add finishing touches and last wave of testing, then release as finished version

import os
import json, random
from collections import deque
from time import sleep

def rules(x):
    print("Hello and Welcome to Untitled Turn-Based Battle version Alpha")
    sleep(x)
    print("\nHow to play:\nFirst, before the battle starts, you select one attack for each category: Weapon, Spell, Shield, Potion, and Finisher. \nDuring the battle, you get to choose your attacks until you run out of stamina points. Then, your opponent does the same. This continues until one of the players lose all of their health, the one who remains is the winner!")
    sleep(x)
    print("\nRules: Both players have 1000 health, or HP and 2 stamina points, or SP. Each attack uses SP from 0.5 to 2. You regain all SP at the end of your turn. Finishers can only be used once per player when they have 500 HP or less, and it uses 2 SP.")
    sleep(x)
    print("\nEffects: \nBurn: lose 50 HP at the end of your turn, lasts 3 turns\nPoison: lose 30 HP at the end of your turn, lasts 5 turns\nBleed: lose 10 HP every turn, lose -10 HP for every hit taken, lasts 10 turns or until healed\nSummon: at the end of your turn, lose 100 HP\n")
    sleep(x)
    print("\nWhen the battle starts, type the attack you want to use and hit enter to use it if posible, enter 'end' to end your turn when you are out of SP")
    sleep(x)

# Load configuration
def load_config():
    with open("config.json") as file:
        print(json.load(file))
        return json.load(file)

# Effects and Actions
class Effect:
    def __init__(self, name, healthchange, turns):
        self.name = name
        self.healthchange = healthchange
        self.turns = turns

class Action:
    def __init__(self, name, type, damage, sp, effect=None, effect_chance=0):
        self.name = name
        self.type = type
        self.damage = damage
        self.sp = sp
        self.effect = effect
        self.effect_chance = effect_chance

# Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 1000
        self.sp = 2.0
        self.effects = deque()
        self.moveset = []

    def apply_effects(self):
        for effect in list(self.effects):
            self.hp += effect.healthchange
            effect.turns -= 1
            if effect.turns <= 0:
                self.effects.remove(effect)

    def add_effect(self, effect):
        self.effects.append(effect)

# Game Class
class Game:
    def __init__(self, config):
        self.config = config
        self.player = None
        self.cpu = None
        self.moves = self.load_moves()

    def load_moves(self):
        moves = {}
        for category in ["weapons", "spells", "shields", "potions", "finishers"]:
            for item in self.config[category]:
                effect = Effect(item["effect"], 0, 0) if item.get("effect") else None
                moves[item["name"]] = Action(
                    item["name"], item["type"], item["damage"], item["stamina_cost"], effect, item.get("effect_chance", 0)
                )
        return moves

    def setup_players(self):
        self.player = Player(input("Enter your username: "))
        self.cpu = Player("CPU")
        self.setup_moveset(self.player, "player")
        self.setup_moveset(self.cpu, "cpu")

    def setup_moveset(self, player, player_type):
        print(f"Setting up {player.name}'s moveset...")
        for category in ["weapons", "spells", "shields", "potions", "finishers"]:
            options = [item["name"] for item in self.config[category]]
            if player_type == "player":
                player.moveset.append(self.select_move(options))
            else:
                player.moveset.append(random.choice(options))
        print(f"{player.name}'s moveset: {player.moveset}")

    def select_move(self, options):
        while True:
            print("Choose one of the following:")
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
        print(f"{self.player.name}'s turn")
        print(f"Available moves: {self.player.moveset}")
        move_name = input("Enter your move: ").upper()
        if move_name in self.moves:
            move = self.moves[move_name]
            self.perform_attack(self.player, self.cpu, move)
        else:
            print("Invalid move!")
        self.player.apply_effects()

    def cpu_turn(self):
        print("CPU's turn")
        move_name = random.choice(self.cpu.moveset)
        move = self.moves[move_name]
        self.perform_attack(self.cpu, self.player, move)
        self.cpu.apply_effects()

    def perform_attack(self, attacker, defender, move):
        if move.sp > attacker.sp:
            print(f"{attacker.name} does not have enough SP to use {move.name}!")
            return
        attacker.sp -= move.sp
        defender.hp -= move.damage
        print(f"{attacker.name} used {move.name} and dealt {move.damage} damage to {defender.name}!")
        if move.effect and random.randint(1, 100) <= move.effect_chance:
            defender.add_effect(move.effect)
            print(f"{defender.name} is now affected by {move.effect.name}!")

    def check_game_over(self):
        if self.player.hp <= 0:
            print("You lost!")
            return True
        elif self.cpu.hp <= 0:
            print("You won!")
            return True
        return False

    def play(self):
        print("Starting the game!")
        rules(0)
        self.setup_players()
        while True:
            self.player_turn()
            if self.check_game_over():
                break
            self.cpu_turn()
            if self.check_game_over():
                break

# Main Execution
if __name__ == "__main__":
    config = load_config()
    game = Game(config)
    game.play()
