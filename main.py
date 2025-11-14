# main.py

from player import Player
from monster import Monster
from moves import Move
from battle import Battle
import random

def main():
    print("=== Monster Trainer Game ===")
    player_name = input("Enter your name: ")

    # Create player
    player = Player(player_name)

    # ---------------- CREATE STARTER MONSTER ----------------
    # Assign starter moves
    starter_moves = [
        Move("Flame Burst", power=10, cost=2, pp=10, description="A burst of fire."),
        Move("Blaze Kick", power=8, cost=1, pp=15, description="A fiery kick attack.")
    ]
    fire_mon = Monster(
        id=1,
        name="Flareon",
        monster_type="Fire",
        health=60,
        level=1,
        moves=starter_moves
    )
    player.catch(fire_mon)

    # Display player's team
    player.view_team()

    # ---------------- CREATE WILD MONSTER ----------------
    wild_moves = [
        Move("Aqua Jet", power=9, cost=2, pp=10, description="A fast water attack."),
        Move("Bubble Beam", power=7, cost=1, pp=15, description="Shoots bubbles at the opponent.")
    ]
    wild_mon = Monster(
        id=2,
        name="Aquarion",
        monster_type="Water",
        health=55,
        level=1,
        moves=wild_moves
    )
    print(f"\nA wild {wild_mon.name} appeared!\n")

    # ---------------- START BATTLE ----------------
    battle = Battle(player, fire_mon, wild_mon)
    battle.start()

if __name__ == "__main__":
    main()
