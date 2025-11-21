# move.py

class Move:
    """
    Represents a Pokémon move.

    Attributes:
        name (str): Name of the move.
        power (int): Damage the move deals.
        max_pp (int): Maximum Power Points for the move.
        current_pp (int): Current Power Points remaining.
    """

    def __init__(self, name, power, max_pp):
        """
        Initializes a Move object with a name, power, and max PP.

        Args:
            name (str): The name of the move.
            power (int): The power of the move.
            max_pp (int): The maximum PP.
        """
        self.name = name
        self.power = power
        self.max_pp = max_pp
        self.current_pp = max_pp

    def use_move(self):
        """
        Uses the move and reduces its PP by 1.

        Returns:
            int: Power of the move if PP is available, otherwise 0.
        """
        if self.current_pp > 0:
            self.current_pp -= 1
            return self.power
        return 0

    def __str__(self):
        """
        Returns a string representation of the move including its PP.

        Returns:
            str: Move name and PP status.
        """
        return f"{self.name} (Power {self.power}, PP {self.current_pp}/{self.max_pp})"
