# monster.py

"""
Monster class for Monster Trainer Game.

Provides HP, level, move list, combat utilities, and management helpers.
"""

from typing import List, Dict
from move import Move
import random


class Monster:
    """
    Represents a battle monster with stats, moves, and combat behavior.
    """

    def __init__(self, name: str, type_: str, max_hp: int, moves: List[Move], level: int = 1):
        """
        Initialize a Monster.

        Args:
            name (str): Monster name.
            type_ (str): Monster type string.
            max_hp (int): Maximum HP.
            moves (List[Move]): List of Move instances.
            level (int): Starting level.
        """
        self.name = name
        self.type = type_
        self.max_hp = int(max_hp)
        self.current_hp = int(max_hp)
        self.level = int(level)
        self.moves: List[Move] = list(moves)

    def take_damage(self, amount: int):
        """
        Apply damage to the monster.

        Args:
            amount (int): Damage amount.
        """
        self.current_hp = max(0, int(self.current_hp - int(amount)))

    def heal(self, amount: int):
        """
        Heal HP up to max_hp.

        Args:
            amount (int): Healing amount.
        """
        if amount <= 0:
            return
        if self.is_fainted():
            # Optional rule: prevent healing fainted monsters unless revive items exist
            return
        self.current_hp = min(self.max_hp, int(self.current_hp + int(amount)))

    def is_fainted(self) -> bool:
        """Return True if current HP is 0."""
        return self.current_hp <= 0

    def reset_stats(self):
        """Reset HP and PP for a fresh encounter or after capture."""
        self.current_hp = self.max_hp
        for mv in self.moves:
            mv.reset_pp()

    def get_moves(self) -> List[Move]:
        """Return current move list."""
        return self.moves

    def choose_move_random(self) -> Move:
        """
        Return a random usable move.
        If no usable moves remain, return a fallback 'Struggle' move.
        """
        usable = [m for m in self.moves if m.is_usable()]
        if not usable:
            return Move("Struggle", power=4, max_pp=9999, type_="Normal")
        return random.choice(usable)

    def add_move(self, move: Move):
        """Add a move to the monster's repertoire."""
        self.moves.append(move)

    def remove_move_by_name(self, name: str) -> bool:
        """
        Remove the first move that matches name.

        Args:
            name (str): Name of the move to remove.
        Returns:
            bool: True if removed, False otherwise.
        """
        for i, m in enumerate(self.moves):
            if m.name == name:
                del self.moves[i]
                return True
        return False

    def level_up(self, amount: int = 1):
        """
        Increase level and scale max HP.

        Args:
            amount (int): Levels to increase.
        """
        if amount <= 0:
            return
        for _ in range(int(amount)):
            self.level += 1
            self.max_hp = max(1, int(self.max_hp * 1.10))
        self.current_hp = min(self.current_hp, self.max_hp)

    def effective_hp_ratio(self) -> float:
        """
        Return current HP / max HP between 0.0 and 1.0.

        Returns:
            float: Ratio of current HP to max HP.
        """
        if self.max_hp <= 0:
            return 0.0
        return float(self.current_hp) / float(self.max_hp)

    def attack(self, target: "Monster", move: Move, crit_chance: float = 0.10) -> Dict:
        """
        Attack a target monster using a move.

        Args:
            target (Monster): Target monster.
            move (Move): Move used in attack.
            crit_chance (float): Probability of critical hit.

        Returns:
            Dict: Outcome with keys:
                - damage (int)
                - critical (bool)
                - multiplier (float)
                - used_pp (int)
        """
        base = move.use_move()
        if base <= 0:
            return {"damage": 0, "critical": False, "multiplier": 0.0, "used_pp": 0}

        type_mult = move.get_multiplier(target.type)
        critical = (random.random() < crit_chance)
        crit_mult = 1.5 if critical else 1.0

        damage = int(base * type_mult * crit_mult)
        target.take_damage(damage)
        return {
            "damage": damage,
            "critical": critical,
            "multiplier": type_mult * crit_mult,
            "used_pp": 1
        }

    def get_summary(self) -> str:
        """Return multi-line summary string for UI including moves."""
        moves_str = ", ".join([mv.get_move_summary() for mv in self.moves])
        return f"{self.name} (Lvl {self.level}) Type:{self.type} HP:{self.current_hp}/{self.max_hp} Moves:[{moves_str}]"

    def get_hp_status(self) -> str:
        """Return a simple HP status string."""
        return f"HP: {self.current_hp}/{self.max_hp}"

    def has_move(self, name: str) -> bool:
        """Return True if the monster knows a move by name."""
        return any(m.name == name for m in self.moves)

    def __str__(self):
        return f"{self.name} ({self.type}) - HP {self.current_hp}/{self.max_hp} Lvl {self.level}"