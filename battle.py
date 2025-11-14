# battle.py

import random

class Battle:
    """Handles turn-based combat between two monsters."""
    
    def __init__(self, player, player_monster, enemy_monster):
        self.player = player                # Player object
        self.player_monster = player_monster  # Monster object
        self.enemy_monster = enemy_monster    # Monster object
        self.turn_number = 1

    # ---------------- CORE METHODS ----------------

    def start(self):
        """Start the battle sequence."""
        print(f"\nBattle: {self.player_monster.name} vs {self.enemy_monster.name}!")
        self.print_status()

        while not self.is_battle_over():
            self.take_turn()

        self.show_battle_result()

    def take_turn(self):
        """Execute one turn of the battle."""
        print(f"\n--- Turn {self.turn_number} ---")

        action = self.player_choose_action()

        if action == "attack":
            self.execute_attack_phase()
        elif action == "item":
            self.use_item_during_battle()
        elif action == "run":
            if self.run_away():
                return

        self.turn_number += 1
        self.print_status()

    def execute_attack_phase(self):
        """Process both monsters attacking based on speed/level."""
        player_move = self.choose_player_move()
        enemy_move = self.choose_enemy_move()

        order = self.decide_turn_order()

        if order == "player":
            self.player_monster.attack(player_move, self.enemy_monster)
            if not self.enemy_monster.is_fainted():
                self.enemy_monster.attack(enemy_move, self.player_monster)
        else:
            self.enemy_monster.attack(enemy_move, self.player_monster)
            if not self.player_monster.is_fainted():
                self.player_monster.attack(player_move, self.enemy_monster)

    # ---------------- LOGIC METHODS ----------------

    def decide_turn_order(self):
        """Decide which monster acts first."""
        if self.player_monster.level >= self.enemy_monster.level:
            return "player"
        return "enemy"

    def choose_player_move(self):
        """Choose a move (currently auto selects random move)."""
        return random.choice(self.player_monster.moves)

    def choose_enemy_move(self):
        """Random move selection for enemy."""
        return random.choice(self.enemy_monster.moves)

    def player_choose_action(self):
        """Placeholder for future menu system."""
        return "attack"

    def use_item_during_battle(self):
        """Use an item on the player's monster."""
        if len(self.player.inventory) == 0:
            print("You have no items!")
            return
        item_name = list(self.player.inventory.keys())[0]
        print(f"Using {item_name}!")
        self.player.use_item(item_name, self.player_monster)

    def run_away(self):
        """Attempt to escape the battle."""
        chance = random.random()
        if chance < 0.6:
            print("You successfully ran away!")
            return True
        print("You failed to run away!")
        return False

    def print_status(self):
        """Print current HP status of both monsters."""
        print(f"{self.player_monster.name}: {self.player_monster.health}/{self.player_monster.max_health} HP")
        print(f"{self.enemy_monster.name}: {self.enemy_monster.health}/{self.enemy_monster.max_health} HP")

    def is_battle_over(self):
        """Return True if either monster fainted."""
        return self.player_monster.is_fainted() or self.enemy_monster.is_fainted()

    def show_battle_result(self):
        """Print the outcome of the battle."""
        print("\n--- Battle Finished ---")
        if self.player_monster.is_fainted():
            print(f"{self.player_monster.name} fainted! You lost the battle.")
        elif self.enemy_monster.is_fainted():
            print(f"You defeated {self.enemy_monster.name}!")
        else:
            print("The battle ended unexpectedly.")
