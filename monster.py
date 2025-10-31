class Monster:
    def __init__(self, name, max_health, attack, speed, monster_type, level=1):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack = attack
        self.speed = speed
        self.type = monster_type
        self.level = level
        self.xp = 0
        self.max_xp = 100
        self.pp = 10

    def level_up(self):
        if self.xp >= self.max_xp:
            self.level += 1
            self.xp = 0
            self.max_health += 10
            self.attack += 2
            print(f"{self.name} leveled up to {self.level}!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} fainted!")
