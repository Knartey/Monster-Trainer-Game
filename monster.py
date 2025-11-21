# monster.py

from move import Move

class Monster:
    """
    Represents a Pokémon/Monster.

    Attributes:
        name (str): Name of the monster.
        type (str): Type of the monster (Fire, Water, grass, electric).
        max_hp (int): Maximum HP.
        current_hp (int): Current HP.
        level (int): Monster level.
        moves (list[Move]): List of Move objects.
    """

    def __init__(self, name, type_, max_hp, moves, level=1):
        """
        Initializes a Monster with name, type, HP, moves, and level.

        Args:
            name (str): Monster name.
            type_ (str): Monster type.
            max_hp (int): Maximum HP.
            moves (list[Move]): List of Move objects.
            level (int, optional): Monster level. Defaults to 1.
        """
        self.name = name
        self.type = type_
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.level = level
        self.moves = moves

    def take_damage(self, damage):
        """
        Reduces the monster's HP by damage amount.

        Args:
            damage (int): Damage to apply.
        """
        self.current_hp = max(self.current_hp - damage, 0)

    def is_fainted(self):
        """
        Checks if the monster has fainted.

        Returns:
            bool: True if current_hp <= 0, else False.
        """
        return self.current_hp <= 0

    def heal(self, amount):
        """
        Heals the monster by a specified amount.

        Args:
            amount (int): HP to restore.
        """
        self.current_hp = min(self.current_hp + amount, self.max_hp)

    def get_moves(self):
        """
        Returns the list of monster moves.

        Returns:
            list[Move]: Monster's moves.
        """
        return self.moves

    def __str__(self):
        """
        Returns a string representation of the monster.

        Returns:
            str: Monster name, type, HP, and level.
        """
        return f"{self.name} ({self.type}) - HP {self.current_hp}/{self.max_hp}, Lvl {self.level}"
