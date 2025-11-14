# item.py

class Item:
    """Represents an item that can heal health, restore PP, or provide effects."""

    def __init__(self, name, heal_amount=0, restore_pp=0, quantity=1):
        self.name = name
        self.heal_amount = heal_amount
        self.restore_pp = restore_pp
        self.quantity = quantity

    # ---------------- USE METHODS ----------------

    def use(self, target):
        """Use this item on a monster."""
        if self.heal_amount > 0:
            target.heal(self.heal_amount)
        if self.restore_pp > 0:
            for move in target.moves:
                move.restore_pp(self.restore_pp)
        print(f"Used {self.name} on {target.name}!")

    def use_in_battle(self, target):
        """Wrapper for battle use."""
        self.use(target)

    # ---------------- INFO METHODS ----------------

    def describe(self):
        """Return a readable string describing the item."""
        return f"{self.name}: Heal +{self.heal_amount}, Restore PP +{self.restore_pp}"

    def is_consumable(self):
        """Return True if the item is used up after use."""
        return True

    def can_use(self, target):
        """Check if item can be used on target."""
        return True  # all items usable for now

    def display_quantity(self):
        """Return readable quantity text."""
        return f"{self.quantity}x {self.name}"

    # ---------------- UPGRADE METHODS ----------------

    def upgrade(self):
        """Increase healing or PP restoration."""
        self.heal_amount += 10
        self.restore_pp += 1
