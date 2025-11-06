# main.py
from player import Player
from monster import Monster
from battle import Battle

def main():
    print("=== Monster Trainer Game ===")
    player_name = input("Enter your name: ")

    # Create player
    player = Player(player_name)

    # Create player's starter monster
    fire_mon = Monster("Flareon", "Fire", level=1)
    player.team.append(fire_mon)
    print(f"{player.name} caught {fire_mon.name}!\n")

    print("Your Team:")
    for mon in player.team:
        print(f"- {mon.name} (HP: {mon.health}/{mon.max_health})")

    # Create a wild monster for battle
    wild_mon = Monster("Aquarion", "Water", level=1)
    print(f"\nA wild {wild_mon.name} appeared!")

    # Start battle
    battle = Battle(player, fire_mon, wild_mon)
    battle.start()

if __name__ == "__main__":
    main()
