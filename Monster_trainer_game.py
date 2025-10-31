#Monster trainer game
class player:
    def __init__(self, name: str, inventory: list):
        self.name = name
        self.inventory = [{item("Monster balls"): 0}, {item("Health potion"): 0}, {item("PP potion"): 0}]
    def train(self, target: "monster"):
        target.xp += monster.max_xp *.25
        target.level_up()
class monster:
    def __init__(self, pp: int, name: str, max_health: int, health: int, level: int, xp: int, max_xp: int, attacks: list, speed: int, type: str):
        self.pp = pp
        self.max_health = max_health
        self.name = name
        self.health = health
        self.level = level
        self.xp = xp
        self.max_xp = max_xp
        self.attacks = attacks
        self.speed = speed
        self.type = type
    def level_up(self):
        if self.xp >= self.max_xp:
            self.level += 1
            self.xp = 0
        
class item:
    def __init__(self, item_name):
        self.item_name = item_name
class battle:
    def __init__(self, player: player, monster1: monster, monster2: monster):
        self.player = player
        self.monster1 = monster1
        self.monster2 = monster2
    def turn(self):
        if self.monster1.speed > self.monster2.speed:
            turn = (self.monster1, self.monster2)
        elif self.monster2.speed > self.monster1.speed:
            turn = (self.monster2, self.monster1)
        elif self.monster1.name < self.monster2.name:
            turn = (self.monster1.name, self.monster2.name)
        else:
            turn = (self.monster2.name, self.monster1.name)
    def use_item(self, item_name, target: monster):
        match item_name:
            case "Monster balls":
                dict1 = player.inventory[0]
                if dict1[item_name] > 0:
                    None
                else:
                    print("You have no monster balls")
            case "Health potion":
                dict2 = player.inventory[1]
                if dict2[item_name] > 0:
                    dict2[item_name] -= 1
                    self.target.health += (target.max_health-target.health)*.75
                else:
                    print("You have no health potions")
            case "PP potion":
                dict3 = player.inventory[2]
                if dict3[item_name] > 0:
                    dict3[item_name] -= 1
                    self.target.pp += 1
        
