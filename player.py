# player.py

from monster import Monster
from item import Item

class Player:
    """
    Represents the player and manages their team and inventory.

    Attributes:
        name (str): Player's name.
        team (list[Monster]): Player's Pokémon team.
        inventory (list[Item]): List of items the player owns.
    """

    def __init__(self, name):
        """
        Initializes a player with a name, empty team, and starter items.

        Args:
            name (str): Player's name.
        """
        self.name = name
        self.team = []
        self.inventory = [
            Item("Monster Ball", quantity=2),
            Item("Health Potion", heal=30, quantity=2),
            Item("PP Potion", restore_pp=5, quantity=1)
        ]

    def add_monster(self, monster):
        """
        Adds a monster to the player's team.

        Args:
            monster (Monster): Monster to add.
        """
        self.team.append(monster)

    def use_item(self, item_index, monster_index):
        """
        Uses an item on a specific monster.

        Args:
            item_index (int): Index of item in inventory.
            monster_index (int): Index of monster in team.
        """
        item = self.inventory[item_index]
        monster = self.team[monster_index]
        heal, restore_pp = item.use()
        monster.heal(heal)
        for move in monster.get_moves():
            move.current_pp = min(move.current_pp + restore_pp, move.max_pp)

    def has_usable_monsters(self):
        """
        Checks if any monsters in the team are alive.

        Returns:
            bool: True if at least one monster has HP > 0.
        """
        return any(m.current_hp > 0 for m in self.team)
