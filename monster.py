# monster.py

from moves import Move

class Monster:
    """Represents a monster with stats, moves, leveling, combat behavior, and status reporting."""

    def __init__(self, id, name, monster_type, health, level, moves):
        self.id = id
        self.name = name
        self.type = monster_type
        self.health = health
        self.max_health = health
        self.level = level
        self.moves = moves  # list of Move objects
        self.xp = 0
        self.max_xp = 100


    # ---------------- BASIC METHODS ----------------

    def assign_moves(self, moves):
        """Assign a list of moves to the monster."""
        self.moves = moves

    def level_up(self):
        """Increase monster level when XP reaches threshold."""
        while self.xp >= self.max_xp:
            self.level += 1
            self.xp -= self.max_xp
            self.max_health += 10
            self.health = self.max_health
            print(f"{self.name} leveled up!")

    def is_fainted(self):
        """Return True if the monster has fainted."""
        return self.health <= 0

    # ---------------- COMBAT METHODS ----------------

    def attack(self, move, target):
        """Attack another monster using a move."""
        if move.pp <= 0:
            print(f"{move.name} has no PP left!")
            return 0

        damage = move.use()
        target.take_damage(damage)
        return damage

    def take_damage(self, amount):
        """Reduce monster health by a damage amount."""
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        """Heal the monster by a given amount."""
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    # ---------------- PROGRESSION METHODS ----------------

    def gain_xp(self, amount):
        """Add XP and handle leveling up."""
        self.xp += amount
        self.level_up()

    def restore_pp(self, move_name, amount):
        """Restore PP for a specific move by name."""
        for m in self.moves:
            if m.name == move_name:
                m.restore_pp(amount)

    # ---------------- INFO METHODS ----------------

    def get_status(self):
        """Return a readable string showing monster status."""
        return f"{self.name} — HP: {self.health}/{self.max_health}, Lvl {self.level}, XP: {self.xp}/{self.max_xp}"
