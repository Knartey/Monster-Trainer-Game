from player import Player
from monster import Monster
from battle import Battle

def main():
    print("=== Monster Trainer Game ===")
    player_name = input("Enter your name: ")
    player = Player(player_name)

    # Starter monsters
    fire_mon = Monster("Flareon", max_health=50, attack=10, speed=7, monster_type="Fire")
    water_mon = Monster("Aquarion", max_health=45, attack=9, speed=8, monster_type="Water")

    player.catch(fire_mon)

    print("\nYour Team:")
    for mon in player.team:
        print(f"- {mon.name} (HP: {mon.health}/{mon.max_health})")

    print("\nA wild Aquarion appeared!")
    battle = Battle(player.team[0], water_mon)
    battle.start()

if __name__ == "__main__":
    main()
