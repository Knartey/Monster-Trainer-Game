import random

class Battle:
    def __init__(self, player_monster, enemy_monster):
        self.player_monster = player_monster
        self.enemy_monster = enemy_monster

    def determine_turn(self):
        if self.player_monster.speed > self.enemy_monster.speed:
            return self.player_monster, self.enemy_monster
        elif self.enemy_monster.speed > self.player_monster.speed:
            return self.enemy_monster, self.player_monster
        else:
            # if speeds equal, randomize who starts
            return random.choice([(self.player_monster, self.enemy_monster),
                                  (self.enemy_monster, self.player_monster)])

    def start(self):
        print(f"Battle: {self.player_monster.name} vs {self.enemy_monster.name}!")
        while self.player_monster.health > 0 and self.enemy_monster.health > 0:
            first, second = self.determine_turn()

            # First attack
            damage = random.randint(1, first.attack)
            second.take_damage(damage)
            print(f"{first.name} attacks {second.name} for {damage} damage!")

            if second.health <= 0:
                print(f"{second.name} fainted! {first.name} wins!")
                break

            # Second attack
            damage = random.randint(1, second.attack)
            first.take_damage(damage)
            print(f"{second.name} attacks {first.name} for {damage} damage!")

            if first.health <= 0:
                print(f"{first.name} fainted! {second.name} wins!")
                break
