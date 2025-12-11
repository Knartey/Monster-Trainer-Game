# move.py

"""
Move class for Monster Trainer Game.

Provides move behavior (PP, power, type), small damage variation,
and helper utilities for UI and testing.
"""

from typing import Tuple
import random

# Type effectiveness chart
TYPE_CHART = {
    "Fire":    {"Grass": 2.0, "Water": 0.5, "Rock": 0.5, "Fire": 0.5},
    "Water":   {"Fire": 2.0, "Rock": 2.0, "Grass": 0.5, "Water": 0.5},
    "Grass":   {"Water": 2.0, "Rock": 2.0, "Fire": 0.5},
    "Electric":{"Water": 2.0, "Electric": 0.5, "Grass": 0.5, "Rock": 0.5},
    "Rock":    {"Fire": 2.0, "Electric": 1.0, "Water": 1.0, "Grass": 1.0},
    "Normal":  {"Rock": 0.5}
}


class Move:
    """
    Represents a combat move with power, PP, and type.
    """

    def __init__(self, name: str, power: int, max_pp: int, type_: str = "Normal"):
        """
        Initialize a Move.

        Args:
            name (str): Move name.
            power (int): Base power.
            max_pp (int): Maximum PP.
            type_ (str): Move type string.
        """
        self.name = name
        self.power = int(power)
        self.max_pp = int(max_pp)
        self.current_pp = int(max_pp)
        self.type = type_

    def use_move(self) -> int:
        """
        Consume 1 PP and return base power.

        Returns:
            int: Power value if usable, 0 if no PP left.
        """
        if self.current_pp <= 0:
            return 0
        self.current_pp -= 1
        return self.power

    def restore_pp(self, amount: int) -> int:
        """
        Restore PP by amount.

        Args:
            amount (int): Amount to restore.

        Returns:
            int: Actual PP restored.
        """
        if amount <= 0:
            return 0
        before = self.current_pp
        self.current_pp = min(self.max_pp, self.current_pp + int(amount))
        return self.current_pp - before

    def reset_pp(self):
        """Reset current PP to max_pp."""
        self.current_pp = self.max_pp

    def is_usable(self) -> bool:
        """Return True if at least 1 PP remains."""
        return self.current_pp > 0

    def get_multiplier(self, defender_type: str) -> float:
        """
        Return type effectiveness multiplier vs defender_type.

        Args:
            defender_type (str): Type of the defending monster.

        Returns:
            float: Effectiveness multiplier.
        """
        return TYPE_CHART.get(self.type, {}).get(defender_type, 1.0)

    def get_damage_range(self, variation_pct: float = 0.1) -> Tuple[int, int]:
        """
        Return a plausible damage range (min, max) given small variation.

        Args:
            variation_pct (float): Variation percentage (default ±10%).

        Returns:
            Tuple[int, int]: Minimum and maximum possible damage.
        """
        if variation_pct < 0:
            variation_pct = 0.0
        delta = max(0, int(self.power * variation_pct))
        return max(0, self.power - delta), self.power + delta

    def get_move_summary(self) -> str:
        """
        Return compact summary useful for UIs.

        Returns:
            str: Summary string with name, type, power, and PP.
        """
        return f"{self.name} ({self.type}) Power:{self.power} PP:{self.current_pp}/{self.max_pp}"

    def pp_percentage(self) -> float:
        """
        Return current PP percentage between 0.0 and 1.0.

        Returns:
            float: PP ratio.
        """
        if self.max_pp <= 0:
            return 0.0
        return self.current_pp / self.max_pp

    def remaining_pp(self) -> int:
        """
        Return current PP as integer.

        Returns:
            int: Current PP.
        """
        return self.current_pp

    def is_type(self, type_name: str) -> bool:
        """
        Check if move matches a given type.

        Args:
            type_name (str): Type to check.

        Returns:
            bool: True if type matches.
        """
        return self.type.lower() == type_name.lower()

    def __str__(self):
        return self.get_move_summary()