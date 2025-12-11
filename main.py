# main.py

"""
Main game loop for Monster Trainer Game.

Uses the updated class APIs (Move, Monster, Item, Player).
"""

from move import Move
from monster import Monster
from player import Player
from item import Item
import random
import copy

# Constants for gameplay mechanics
CRITICAL_CHANCE = 0.10
RUN_SUCCESS_BASE = 0.70


def create_default_moves():
    """Return dict of move prototypes (fresh instances should be deep-copied)."""
    return {
        "Flame Burst": Move("Flame Burst", power=10, max_pp=10, type_="Fire"),
        "Blaze Kick": Move("Blaze Kick", power=8, max_pp=15, type_="Fire"),
        "Bubble Beam": Move("Bubble Beam", power=7, max_pp=10, type_="Water"),
        "Aqua Jet": Move("Aqua Jet", power=9, max_pp=10, type_="Water"),
        "Rock Smash": Move("Rock Smash", power=12, max_pp=8, type_="Rock"),
        "Thunder Shock": Move("Thunder Shock", power=10, max_pp=10, type_="Electric"),
        "Tackle": Move("Tackle", power=8, max_pp=25, type_="Normal"),
    }


def create_monsters(move_prototypes):
    """Return base monster prototypes (deep copies are used when spawning)."""
    return [
        Monster("Flareon", "Fire", 60, [
            copy.deepcopy(move_prototypes["Flame Burst"]),
            copy.deepcopy(move_prototypes["Blaze Kick"]),
            copy.deepcopy(move_prototypes["Tackle"])
        ]),
        Monster("Aquarion", "Water", 55, [
            copy.deepcopy(move_prototypes["Bubble Beam"]),
            copy.deepcopy(move_prototypes["Aqua Jet"]),
            copy.deepcopy(move_prototypes["Tackle"])
        ]),
        Monster("Terrax", "Rock", 80, [
            copy.deepcopy(move_prototypes["Rock Smash"]),
            copy.deepcopy(move_prototypes["Tackle"])
        ]),
        Monster("Voltaris", "Electric", 50, [
            copy.deepcopy(move_prototypes["Thunder Shock"]),
            copy.deepcopy(move_prototypes["Tackle"])
        ]),
    ]


def display_menu():
    """Display main menu options."""
    print("\n=== Monster Trainer Game ===")
    print("1. Start Encounter (Choose a monster and face a wild one)")
    print("2. Show Instructions")
    print("3. Show Team & Inventory")
    print("4. Exit")


def display_instructions():
    """Display game instructions."""
    print("\n=== Instructions ===")
    print("- Choose one of your monsters to encounter a wild one.")
    print("- In battle choose Attack, Use Item, or Run.")
    print("- Monster Ball can capture weakened wild monsters.")
    print("- Type advantages and critical hits affect damage.")
    print("- After each wild encounter the monsters will have their HP/PP reset.")


def show_team_and_inventory(player: Player):
    """Display player's team and inventory."""
    print(f"\n{player.name}'s Team:")
    if not player.team:
        print(" - no monsters")
    else:
        for i, m in enumerate(player.team, 1):
            print(f" {i}. {m.get_summary()}")

    print("\nInventory:")
    if not player.inventory:
        print(" - empty")
    else:
        for i, it in enumerate(player.inventory, 1):
            print(f" {i}. {it.get_item_summary()}")


def try_to_run(player_monster: Monster, wild_monster: Monster) -> bool:
    """Compute run success using base and level modifier."""
    base = RUN_SUCCESS_BASE
    level_diff = wild_monster.level - player_monster.level
    modifier = 0.05 * level_diff
    chance = max(0.1, min(0.95, base - modifier))
    return random.random() < chance


def calculate_capture_chance(wild: Monster, used_item: Item) -> float:
    """Calculate simple capture probability depending on HP ratio and item."""
    hp_ratio = wild.effective_hp_ratio()
    base_chance = 0.35
    chance = base_chance + (1.0 - hp_ratio) * 0.50
    if not used_item.is_capture_item():
        chance *= 0.1
    return max(0.01, min(0.95, chance))


def battle_encounter(player: Player, player_monster: Monster, wild_monster: Monster):
    """
    Conduct a single wild encounter between player's chosen monster and a wild one.
    Handles attack, item use, capture, and run attempts.
    """
    print(f"\nA wild {wild_monster.name} appeared!")
    wild_monster.reset_stats()
    player_monster.reset_stats()
    turn = 1
    caught = False

    while not player_monster.is_fainted() and not wild_monster.is_fainted() and not caught:
        print(f"\n--- Turn {turn} ---")
        print(f"{player_monster.name}: {player_monster.current_hp}/{player_monster.max_hp} HP")
        print(f"{wild_monster.name}: {wild_monster.current_hp}/{wild_monster.max_hp} HP")
        print("\nChoose Action:")
        print("1. Attack")
        print("2. Use Item")
        print("3. Run")

        action = input("Enter 1-3: ").strip()

        if action == "1":
            # Player attack
            for i, mv in enumerate(player_monster.get_moves(), 1):
                print(f"{i}. {mv.get_move_summary()}")
            choice = input("Choose move number: ").strip()
            if not (choice.isdigit() and 1 <= int(choice) <= len(player_monster.get_moves())):
                print("Invalid move; turn wasted.")
            else:
                mv = player_monster.get_moves()[int(choice) - 1]
                outcome = player_monster.attack(wild_monster, mv, crit_chance=CRITICAL_CHANCE)
                if outcome["used_pp"] == 0:
                    print(f"{player_monster.name} tried to use {mv.name} but had no PP!")
                else:
                    print(f"{player_monster.name} used {mv.name}!")
                    if outcome["critical"]:
                        print("A critical hit!")
                    if outcome["multiplier"] > 1.0:
                        print("It's super effective!")
                    elif outcome["multiplier"] < 1.0:
                        print("It's not very effective...")
                    print(f"It dealt {outcome['damage']} damage!")

        elif action == "2":
            # Item usage
            if not player.inventory:
                print("You have no items.")
            else:
                print("\nInventory:")
                for i, it in enumerate(player.inventory, 1):
                    print(f"{i}. {it.get_item_summary()}")
                item_choice = input("Enter item number to use: ").strip()
                if not (item_choice.isdigit() and 1 <= int(item_choice) <= len(player.inventory)):
                    print("Invalid item selection.")
                else:
                    item_idx = int(item_choice) - 1
                    item_obj = player.inventory[item_idx]
                    if item_obj.is_capture_item():
                        chance = calculate_capture_chance(wild_monster, item_obj)
                        roll = random.random()
                        item_obj.use()
                        if roll < chance:
                            print(f"You threw a {item_obj.name}... and captured {wild_monster.name}!")
                            player.add_monster_deepcopy(wild_monster)
                            caught = True
                        else:
                            print("The Monster Ball failed to capture it.")
                    else:
                        if not player.team:
                            print("You have no monsters to use that on.")
                        else:
                            print("\nChoose a team monster to apply the item:")
                            for i, tm in enumerate(player.team, 1):
                                print(f"{i}. {tm}")
                            mi = input("Enter monster number: ").strip()
                            if not (mi.isdigit() and 1 <= int(mi) <= len(player.team)):
                                print("Invalid monster selection.")
                            else:
                                success, msg = player.use_item_on_monster(item_idx, int(mi) - 1)
                                print(msg)

        elif action == "3":
            # Run attempt
            if try_to_run(player_monster, wild_monster):
                print("You successfully ran away!")
                break
            else:
                print("Couldn't escape!")

        else:
            print("Invalid action; turn wasted.")

                # Wild monster turn
        if wild_monster.is_fainted():
            print(f"\nThe wild {wild_monster.name} fainted!")
            break

        opp_move = wild_monster.choose_move_random()
        outcome = wild_monster.attack(player_monster, opp_move, crit_chance=CRITICAL_CHANCE)
        if outcome["used_pp"] == 0:
            print(f"The wild {wild_monster.name} tried {opp_move.name} but had no PP!")
        else:
            print(f"The wild {wild_monster.name} used {opp_move.name}!")
            if outcome["critical"]:
                print("A critical hit from the wild monster!")
            if outcome["multiplier"] > 1.0:
                print("It's super effective against you!")
            elif outcome["multiplier"] < 1.0:
                print("It's not very effective...")
            print(f"It dealt {outcome['damage']} damage!")

        if player_monster.is_fainted():
            print(f"\n{player_monster.name} fainted! You lost this encounter.")
            break

        turn += 1

    # Post encounter reset
    player_monster.reset_stats()
    wild_monster.reset_stats()


def main():
    """Entry point for the Monster Trainer game loop."""
    move_protos = create_default_moves()
    base_monsters = create_monsters(move_protos)

    player_name = input("Enter your name: ").strip() or "Trainer"
    player = Player(player_name)

    # Give starter monster
    starter = copy.deepcopy(base_monsters[0])
    starter.level = 1
    player.add_monster(starter)
    print(f"\nWelcome {player.name}! You received a starter: {starter.name}.\n")

    while True:
        display_menu()
        option = input("Choose an option (1-4): ").strip()
        if option == "1":
            if not player.team:
                print("You have no monsters to start an encounter.")
                continue
            print("\nChoose one of your monsters to send out:")
            for i, tm in enumerate(player.team, 1):
                print(f"{i}. {tm}")
            sel = input("Enter number: ").strip()
            if not (sel.isdigit() and 1 <= int(sel) <= len(player.team)):
                print("Invalid selection.")
                continue
            chosen_idx = int(sel) - 1
            player_mon = player.team[chosen_idx]
            wild_proto = random.choice(base_monsters)
            wild_mon = copy.deepcopy(wild_proto)
            battle_encounter(player, player_mon, wild_mon)
            print("\n--- After Encounter ---")
            show_team_and_inventory(player)

        elif option == "2":
            display_instructions()

        elif option == "3":
            show_team_and_inventory(player)

        elif option == "4":
            print("Goodbye Trainer!")
            break

        else:
            print("Invalid selection. Enter 1-4.")


if __name__ == "__main__":
    main()
       