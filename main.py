"""
Monster Trainer Game
-------------------
A text-based Pokémon-style game where players can choose monsters, battle opponents,
and use items. Demonstrates object-oriented programming, class interactions,
and user input handling in Python.
"""

from move import Move
from monster import Monster
from player import Player
from item import Item
import random


def create_default_moves():
    """
    Creates the default moves for monsters.
    """
    return {
        "Flame Burst": Move("Flame Burst", power=10, max_pp=10),
        "Blaze Kick": Move("Blaze Kick", power=8, max_pp=15),
        "Bubble Beam": Move("Bubble Beam", power=7, max_pp=10),
        "Aqua Jet": Move("Aqua Jet", power=9, max_pp=10),
        "Rock Smash": Move("Rock Smash", power=12, max_pp=8),
        "Thunder Shock": Move("Thunder Shock", power=10, max_pp=10),
        "Tackle": Move("Tackle", power=5, max_pp=25),
    }


def create_monsters(moves):
    """
    Creates the default monsters for the game.
    """
    return [
        Monster("Flareon", "Fire", 60, [moves["Flame Burst"], moves["Blaze Kick"], moves["Tackle"]]),
        Monster("Aquarion", "Water", 55, [moves["Bubble Beam"], moves["Aqua Jet"], moves["Tackle"]]),
        Monster("Terrax", "Rock", 80, [moves["Rock Smash"], moves["Tackle"]]),
        Monster("Voltaris", "Electric", 50, [moves["Thunder Shock"], moves["Tackle"]]),
    ]


def display_menu():
    print("\n=== Monster Trainer Game ===")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Exit")


def display_instructions():
    print("\n=== Instructions ===")
    print("- Choose your Pokémon.")
    print("- Choose an opponent Pokémon.")
    print("- In battle, you can Attack, Use Item, or Run.")
    print("- Use items to heal or restore PP.")
    print("- Gain XP to level up your Pokémon.")


def choose_monster(monsters):
    while True:
        print("\n=== Choose Your Pokémon ===")
        for i, m in enumerate(monsters, 1):
            print(f"{i}. {m.name} ({m.type}) - HP {m.current_hp}")
        choice = input("Enter Pokémon number: ")

        if choice.isdigit() and 1 <= int(choice) <= len(monsters):
            return monsters[int(choice) - 1]

        print("Invalid Pokémon! Try again.")


def choose_opponent(monsters):
    while True:
        print("\n=== Choose an Opponent Pokémon ===")
        for i, m in enumerate(monsters, 1):
            print(f"{i}. {m.name} ({m.type}) - HP {m.current_hp}")
        choice = input("Enter Pokémon number: ")

        if choice.isdigit() and 1 <= int(choice) <= len(monsters):
            return monsters[int(choice) - 1]

        print("Invalid Pokémon! Try again.")


def battle(player_monster, opponent_monster):
    turn = 1
    caught = False

    while not player_monster.is_fainted() and not opponent_monster.is_fainted() and not caught:
        print(f"\n--- Turn {turn} ---")
        print(f"{player_monster.name}: {player_monster.current_hp}/{player_monster.max_hp} HP")
        print(f"{opponent_monster.name}: {opponent_monster.current_hp}/{opponent_monster.max_hp} HP")

        print("\nChoose Action:")
        print("1. Attack")
        print("2. Use Item")
        print("3. Run")
        action = input("Enter 1-3: ")

        if action == "1":
            for i, move in enumerate(player_monster.moves, 1):
                print(f"{i}. {move}")

            move_choice = input("Enter move number: ")

            if move_choice.isdigit() and 1 <= int(move_choice) <= len(player_monster.moves):
                move = player_monster.moves[int(move_choice) - 1]
                damage = move.use_move()
                opponent_monster.take_damage(damage)
                print(f"{player_monster.name} used {move.name} and dealt {damage} damage!")

            opp_move = opponent_monster.moves[0]
            damage = opp_move.use_move()
            player_monster.take_damage(damage)
            print(f"{opponent_monster.name} used {opp_move.name} and dealt {damage} damage!")

        elif action == "2":
            print("\nChoose an Item:")
            for i, item in enumerate(player.inventory, 1):
                print(f"{i}. {item}")

            item_choice = input("Enter item number: ")

            if item_choice.isdigit() and 1 <= int(item_choice) <= len(player.inventory):
                item_index = int(item_choice) - 1
                player.use_item(item_index, 0)

                if item_index == 0:  # Monster Ball
                    catch_chance = random.randint(0, 100)
                    if catch_chance < 35:
                        caught = True
                        print(f"You caught {opponent_monster.name}!")
                        player.add_monster(opponent_monster)
                    else:
                        print("The Monster Ball failed!")
                else:
                    print(f"Used {player.inventory[item_index].name}!")

        elif action == "3":
            print("You successfully ran away!")
            break

        else:
            print("Invalid input! Enter 1–3.")

        turn += 1

    # Final result
    if player_monster.is_fainted():
        print(f"\n--- Battle Finished ---\n{player_monster.name} fainted! You lost.")
    elif opponent_monster.is_fainted():
        print(f"\n--- Battle Finished ---\nYou defeated {opponent_monster.name}!")
        print(f"{player_monster.name} gained 50 XP!")
    elif caught:
        print(f"\n--- Battle Finished ---\n{opponent_monster.name} was caught!")


def main():
    moves = create_default_moves()
    monsters = create_monsters(moves)

    player_name = input("Enter your name: ")
    global player
    player = Player(player_name)

    while True:
        display_menu()
        option = input("Choose an option (1-3): ")

        if option == "1":
            player_monster = choose_monster(monsters)
            player.add_monster(player_monster)
            print(f"\n{player.name} caught {player_monster.name}!")

            print("\nYour Team:")
            for m in player.team:
                print(m)

            print("\nYour Inventory:")
            for item in player.inventory:
                print(f" - {item}")

            opponent_monster = random.choice(monsters)
            print(f"\nA wild {opponent_monster.name} appeared!")
            battle(player_monster, opponent_monster)

            print("\nYour Team after battle:")
            for m in player.team:
                print(m)

            print("\nYour Inventory after battle:")
            for item in player.inventory:
                print(f" - {item}")

        elif option == "2":
            display_instructions()

        elif option == "3":
            print("Goodbye Trainer!")
            break

        else:
            print("Invalid input! Enter 1–3.")


if __name__ == "__main__":
    main()
