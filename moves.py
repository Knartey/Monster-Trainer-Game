# moves.py
# Defines individual monster moves with power, PP, and type.

class Move:
    def __init__(self, name, power, move_type, max_pp):
        self.name = name
        self.power = power
        self.move_type = move_type
        self.pp = max_pp
        self.max_pp = max_pp

    def use(self, user, target):
        """Execute the move, reducing PP and damaging the target."""
        if self.pp <= 0:
            print(f"{user.name} has no PP left for {self.name}!")
            return

        self.pp -= 1
        damage = int(self.power + (user.level * 0.5))
        target.health = max(0, target.health - damage)
        print(f"{user.name} used {self.name}! It dealt {damage} damage.")
