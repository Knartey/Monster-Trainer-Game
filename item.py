# item.py

"""
Item class for Monster Trainer Game.

Items can heal HP, restore PP, or be capture items.
Includes helper methods to inspect and apply effects.
"""

from typing import Tuple


class Item:
    """
    Represents a consumable item with healing, PP restoration, or capture effects.
    """

    def __init__(self, name: str, heal: int = 0, restore_pp: int = 0,
                 quantity: int = 1, is_capture: bool = False):
        """
        Initialize an Item.

        Args:
            name (str): Item name.
            heal (int): HP restored.
            restore_pp (int): PP restored per move.
            quantity (int): Number available.
            is_capture (bool): Whether item is for capturing monsters.
        """
        self.name = name
        self.heal = int(heal)
        self.restore_pp = int(restore_pp)
        self.quantity = int(quantity)
        self.is_capture = bool(is_capture)

    def use(self) -> Tuple[int, int]:
        """
        Consume one item and return effects (heal, restore_pp).

        Returns:
            Tuple[int, int]: (heal, restore_pp). If none left, returns (0, 0).
        """
        if self.quantity <= 0:
            return 0, 0
        self.quantity -= 1
        return self.heal, self.restore_pp

    def increase_quantity(self, n: int = 1):
        """
        Increase stack quantity by n.

        Args:
            n (int): Amount to increase. No-op if n <= 0.
        """
        if n <= 0:
            return
        self.quantity += int(n)

    def is_usable(self) -> bool:
        """Return True if at least one item remains in stack."""
        return self.quantity > 0

    def is_healing_item(self) -> bool:
        """Return True if this item heals HP."""
        return self.heal > 0 and not self.is_capture

    def is_pp_item(self) -> bool:
        """Return True if this item restores PP."""
        return self.restore_pp > 0 and not self.is_capture

    def is_capture_item(self) -> bool:
        """Return True if this item is intended to capture monsters."""
        return self.is_capture

    def get_kind(self) -> str:
        """
        Return item kind string for UI.

        Returns:
            str: "Capture", "Heal", "PP Restore", or "Misc".
        """
        if self.is_capture:
            return "Capture"
        if self.is_healing_item():
            return "Heal"
        if self.is_pp_item():
            return "PP Restore"
        return "Misc"

    def can_use_on(self, monster) -> bool:
        """
        Determine whether this item can be applied to the given monster.

        Args:
            monster (Monster): Target monster.

        Returns:
            bool: True if applicable, False otherwise.
        """
        if self.is_capture:
            return False
        # healing and PP items always applicable unless monster is fainted
        return not getattr(monster, "is_fainted", lambda: False)()

    def apply_effect(self, monster) -> Tuple[int, int]:
        """
        Apply effects to a Monster instance.

        Args:
            monster (Monster): Target monster.

        Returns:
            Tuple[int, int]: (healed_amount, total_pp_restored).
        """
        if not self.is_usable():
            return 0, 0
        heal, restore_pp = self.use()
        healed = 0
        restored_total = 0
        if heal > 0 and not monster.is_fainted():
            before = getattr(monster, "current_hp", 0)
            monster.heal(heal)
            after = getattr(monster, "current_hp", before)
            healed = after - before
        if restore_pp > 0:
            for move in getattr(monster, "get_moves", lambda: [])():
                restored_total += move.restore_pp(restore_pp)
        return healed, restored_total

    def get_item_summary(self) -> str:
        """
        Return UI-friendly description.

        Returns:
            str: Summary string with quantity, name, kind, heal, and PP values.
        """
        return f"{self.quantity}x {self.name} [{self.get_kind()}] (Heal:{self.heal} PP:{self.restore_pp})"

    def __str__(self):
        return self.get_item_summary()