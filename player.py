# player.py

"""
Player class for Monster Trainer Game.

Manages team, inventory, and player actions (item use, team manipulation).
"""

from typing import List
from monster import Monster
from item import Item
import copy


class Player:
    """
    Represents a player with a team of monsters and an inventory of items.
    """

    def __init__(self, name: str):
        """
        Initialize player with starter inventory and empty team.

        Args:
            name (str): Player's name.
        """
        self.name = name
        self.team: List[Monster] = []
        self.inventory: List[Item] = [
            Item("Monster Ball", quantity=2, is_capture=True),
            Item("Health Potion", heal=30, quantity=2),
            Item("PP Potion", restore_pp=5, quantity=1),
        ]

    def add_monster(self, monster: Monster):
        """
        Add a Monster instance directly.

        Args:
            monster (Monster): Monster to add.
        """
        self.team.append(monster)

    def add_monster_deepcopy(self, monster: Monster):
        """
        Add a deep copy of monster to avoid shared state.

        Args:
            monster (Monster): Monster to copy and add.
        """
        self.team.append(copy.deepcopy(monster))

    def remove_monster_by_index(self, index: int) -> bool:
        """
        Remove monster at index.

        Args:
            index (int): Index of monster in team.

        Returns:
            bool: True if removed, False otherwise.
        """
        if 0 <= index < len(self.team):
            del self.team[index]
            return True
        return False

    def add_item(self, item: Item):
        """
        Add an item to inventory; merge if same-name item exists.

        Args:
            item (Item): Item to add.
        """
        for it in self.inventory:
            if it.name == item.name and it.get_kind() == item.get_kind():
                it.increase_quantity(item.quantity)
                return
        self.inventory.append(item)

    def remove_item_by_index(self, index: int) -> bool:
        """
        Remove item by index from inventory.

        Args:
            index (int): Index of item in inventory.

        Returns:
            bool: True if removed, False otherwise.
        """
        if 0 <= index < len(self.inventory):
            del self.inventory[index]
            return True
        return False

    def use_item_on_monster(self, item_index: int, monster_index: int) -> tuple[bool, str]:
        """
        Use non-capture item on a team monster.

        Args:
            item_index (int): Index of item in inventory.
            monster_index (int): Index of monster in team.

        Returns:
            tuple[bool, str]: Success flag and descriptive message.
        """
        if item_index < 0 or item_index >= len(self.inventory):
            return False, "Invalid item selection."
        if monster_index < 0 or monster_index >= len(self.team):
            return False, "Invalid monster selection."

        item = self.inventory[item_index]
        if item.is_capture_item():
            return False, "Cannot use capture items on own monsters."

        if not item.is_usable():
            return False, f"No {item.name}s left."

        healed, restored = item.apply_effect(self.team[monster_index])
        parts = []
        if healed:
            parts.append(f"{self.team[monster_index].name} healed {healed} HP.")
        if restored:
            parts.append(f"Restored {restored} PP across moves.")
        if not parts:
            parts.append(f"{item.name} had no effect.")
        return True, " ".join(parts)

    def find_item_by_name(self, name: str) -> int:
        """
        Find item index by name.

        Args:
            name (str): Item name to search.

        Returns:
            int: Index of first matching item, -1 if not found.
        """
        for idx, it in enumerate(self.inventory):
            if it.name.lower() == name.lower():
                return idx
        return -1

    def inventory_list(self) -> List[str]:
        """
        Return list of printable inventory strings.

        Returns:
            List[str]: Inventory summaries.
        """
        return [it.get_item_summary() for it in self.inventory]

    def team_list(self) -> List[str]:
        """
        Return list of printable team member summaries.

        Returns:
            List[str]: Team summaries.
        """
        return [m.get_summary() for m in self.team]

    def has_usable_monsters(self) -> bool:
        """
        Return True if any monster in team is not fainted.

        Returns:
            bool: True if at least one monster is usable.
        """
        return any(not m.is_fainted() for m in self.team)

    def total_team_health(self) -> int:
        """
        Return sum of current HP for all team monsters.

        Returns:
            int: Total HP.
        """
        return sum(m.current_hp for m in self.team)

    def get_team_size(self) -> int:
        """Return number of monsters in team."""
        return len(self.team)

    def get_inventory_size(self) -> int:
        """Return number of items in inventory."""
        return len(self.inventory)

    def __str__(self):
        return f"Player {self.name} | Team size: {len(self.team)} | Items: {len(self.inventory)}"