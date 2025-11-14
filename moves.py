# moves.py

class Move:
    """Represents a combat move with power, cost, PP, and upgrade behavior."""

    def __init__(self, name, power, cost, pp, description=""):
        self.name = name
        self.power = power
        self.cost = cost
        self.pp = pp
        self.max_pp = pp
        self.description_text = description

    # ---------------- BASIC METHODS ----------------

    def use(self):
        """Consume PP and return damage value."""
        if self.pp > 0:
            self.pp -= 1
            return self.power
        print(f"{self.name} has no PP left!")
        return 0

    def restore_pp(self, amount):
        """Restore PP for this move."""
        self.pp += amount
        if self.pp > self.max_pp:
            self.pp = self.max_pp

    def describe(self):
        """Return a text description of the move."""
        return f"{self.name}: {self.description_text} (Power {self.power}, PP {self.pp}/{self.max_pp})"

    # ---------------- CLASSIFICATION METHODS ----------------

    def is_special(self):
        """Determine if a move is considered special (placeholder logic)."""
        # Example rule: special if cost > 3
        return self.cost > 3

    def is_usable(self):
        """Return True if the move has PP remaining."""
        return self.pp > 0

    # ---------------- UPGRADE METHODS ----------------

    def upgrade(self):
        """Increase the move's power and max PP."""
        self.power += 5
        self.max_pp += 1
        self.pp = self.max_pp  # restore PP on upgrade

    def reset_pp(self):
        """Completely restore PP to full."""
        self.pp = self.max_pp

    def reduced_power_version(self, percent):
        """Return how strong the move would be after applying a percentage reduction."""
        return int(self.power * percent)

    def get_summary(self):
        """Return a readable summary for menus."""
        return f"{self.name} (Power {self.power}, PP {self.pp}/{self.max_pp})"
