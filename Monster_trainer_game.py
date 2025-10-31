#Monster trainer game
class player:
    #Future note: Put items into the item class rather than initialized in the player class
    def __init__(self, monster_balls, health_potion, pp_potion, name: str, inventory: list):
        self.name = name
        self.monster_balls = item("Monster balls")
        self.health_potion = item("Health potion")
        self.pp_potion = item("PP potion")
        self.inventory = [{monster_balls: 0}, {health_potion: 0}, {pp_potion: 0}]
    def train(self, target: "monster"):
        target.xp += monster.max_xp *.25
        target.level_up()
class monster:
    def __init__(self, moves: [], pp: int, name: str, max_health: int, health: int, level: int, xp: int, max_xp: int, attacks: list, speed: int, type: str):
        self.moves = moves
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
    def __init__(self, item_name, pp):
        self.item_name = item_name
        self.pp = pp
    def use(self, target: monster):
        if target.pp > 0:
            target.pp -= 1
        else:
            print("No  more pp")
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
    def use_item(self, item_name: str, target: monster):
        match item_name:
            case "Monster balls":
                dict1 = player.inventory[0]
                if dict1[player.monster_balls] > 0:
                    None
                else:
                    print("You have no monster balls")
            case "Health potion":
                dict2 = player.inventory[1]
                if dict2[player.health_potion] > 0:
                    dict2[player.health_potion] -= 1
                    target.health += (target.max_health-target.health)*.75
                else:
                    print("You have no health potions")
            #Future note: Each move has pp, adds pp to a move
            case "PP potion":
                dict3 = player.inventory[2]
                if dict3[player.pp_potion] > 0:
                    dict3[player.pp_potion] -= 1
                    None
#Future note: Add moves class      
