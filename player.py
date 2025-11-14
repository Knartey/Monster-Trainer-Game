# player.py

from item import Item

class Player:
    """Represents a player who owns monsters, items, and interacts with the game world."""

    def __init__(self, name):
        self.name = name
        self.inventory = {
            "Monster ball": 3,
            "Health potion": 2,
            "PP potion": 1
        }
        self.team = []

    def catch(self, monster):
        """Attempt to catch a monster and add it to the team."""
        if self.inventory["Monster ball"] > 0:
            self.team.append(monster)
            self.inventory["Monster ball"] -= 1
            print(f"{self.name} caught {monster.name}!")
        else:
            print("You have no Monster balls left!")

    def train(self, target):
        """Train and give XP to a monster."""
        target.xp += target.max_xp * 0.25
        target.level_up()

    def use_item(self, item_name, target):
        """Use an item from the inventory on a target monster."""
        if item_name not in self.inventory or self.inventory[item_name] <= 0:
            print(f"No {item_name}s left!")
            return

        if item_name == "Health potion":
            item = Item(item_name, heal_amount=30)
        elif item_name == "PP potion":
            item = Item(item_name, restore_pp=5)
        else:
            print("Unknown item!")
            return

        item.use(target)
        self.inventory[item_name] -= 1


    def view_team(self):
        """Print the player's entire monster team."""
        print("\nYour Team:")
        for i, mon in enumerate(self.team):
            print(f"{i + 1}. {mon.name} (HP: {mon.health}/{mon.max_health}, Lvl {mon.level})")

    def view_inventory(self):
        """Print the player's inventory items."""
        print("\nInventory:")
        for item, qty in self.inventory.items():
            print(f"- {item}: {qty}")

    def choose_monster(self, index):
        """Return the monster at the chosen index."""
        if 0 <= index < len(self.team):
            return self.team[index]
        print("Invalid monster index!")

    def switch_monster(self, current_index, new_index):
        """Switch two monsters in the player's team."""
        if new_index >= len(self.team) or current_index >= len(self.team):
            print("Invalid switch indexes.")
            return
        self.team[current_index], self.team[new_index] = self.team[new_index], self.team[current_index]

    def add_item(self, item_name, amount=1):
        """Add an item to the player's inventory."""
        self.inventory[item_name] = self.inventory.get(item_name, 0) + amount

    def remove_item(self, item_name, amount=1):
        """Remove an item from the player's inventory."""
        if item_name in self.inventory and self.inventory[item_name] >= amount:
            self.inventory[item_name] -= amount
        else:
            print("Cannot remove item — not enough quantity.")

