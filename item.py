# item.py

class Item:
    """
    Represents an item in the player's inventory.

    Attributes:
        name (str): Name of the item.
        heal (int): Amount of HP it heals.
        restore_pp (int): Amount of PP it restores.
        quantity (int): Number of items available.
    """

    def __init__(self, name, heal=0, restore_pp=0, quantity=1):
        """
        Initializes an item with healing/PP values and quantity.

        Args:
            name (str): Item name.
            heal (int, optional): HP to restore. Defaults to 0.
            restore_pp (int, optional): PP to restore. Defaults to 0.
            quantity (int, optional): Number of items. Defaults to 1.
        """
        self.name = name
        self.heal = heal
        self.restore_pp = restore_pp
        self.quantity = quantity

    def use(self):
        """
        Uses the item, reducing its quantity by 1.

        Returns:
            tuple[int, int]: Amount of HP and PP restored.
        """
        if self.quantity > 0:
            self.quantity -= 1
            return self.heal, self.restore_pp
        return 0, 0

    def __str__(self):
        """
        Returns string representation of the item.

        Returns:
            str: Name and quantity of the item.
        """
        return f"{self.quantity}x {self.name}"
