# monster.py
from moves import Move

class Monster:
    def __init__(self, name: str, monster_type: str, level: int = 1):
        self.name = name
        self.type = monster_type
        self.level = level
        self.max_health = 50 + (level * 10)
        self.health = self.max_health
        self.xp = 0
        self.max_xp = 50
        self.speed = 10 + (level * 2)

        # Assign moves dynamically based on type
        self.moves = self.assign_moves(monster_type)

    def assign_moves(self, monster_type):
        """Assign type-specific moves."""
        if monster_type == "Fire":
            return [
                Move("Flame Burst", 10, "Fire", 10),
                Move("Blaze Kick", 8, "Fire", 15)
            ]
        elif monster_type == "Water":
            return [
                Move("Aqua Jet", 9, "Water", 10),
                Move("Bubble Beam", 7, "Water", 15)
            ]
        elif monster_type == "Grass":
            return [
                Move("Leaf Blade", 9, "Grass", 10),
                Move("Vine Whip", 6, "Grass", 15)
            ]
        else:
            return [Move("Tackle", 5, "Normal", 20)]

    def level_up(self):
        if self.xp >= self.max_xp:
            self.level += 1
            self.xp = 0
            self.max_health += 10
            self.health = self.max_health
            print(f"{self.name} leveled up to Level {self.level}!")

    def is_fainted(self):
        return self.health <= 0
