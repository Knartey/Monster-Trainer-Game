# player.py
from item import Item

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {
            "Monster ball": 3,
            "Health potion": 2,
            "PP potion": 1
        }
        self.team = []

    def catch(self, monster):
        if self.inventory["Monster ball"] > 0:
            self.team.append(monster)
            self.inventory["Monster ball"] -= 1
            print(f"{self.name} caught {monster.name}!")
        else:
            print("You have no Monster balls left!")

    def train(self, target):
        target.xp += target.max_xp * 0.25
        target.level_up()

    def use_item(self, item_name, target):
        if item_name not in self.inventory or self.inventory[item_name] <= 0:
            print(f"No {item_name}s left!")
            return

        if item_name == "Health potion":
            item = Item(item_name, heal_amount=30)
            item.use(target)
        elif item_name == "PP potion":
            item = Item(item_name, restore_pp=5)
            item.use(target)

        self.inventory[item_name] -= 1
