class Item:
    def __init__(self, name, heal_amount=0, restore_pp=0):
        self.name = name
        self.heal_amount = heal_amount
        self.restore_pp = restore_pp

    def use(self, target):
        if self.heal_amount > 0:
            healed = min(target.max_health - target.health, self.heal_amount)
            target.health += healed
            print(f"{target.name} healed by {healed} HP!")
        if self.restore_pp > 0:
            target.pp += self.restore_pp
            print(f"{target.name} restored {self.restore_pp} PP!")
