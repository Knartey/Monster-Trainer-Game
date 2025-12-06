# move.py

TYPE_CHART = {
    "Fire": {
        "Grass": 2.0,
        "Water": 0.5,
        "Rock": 0.5,
        "Fire": 0.5
    },
    "Water": {
        "Fire": 2.0,
        "Rock": 2.0,
        "Grass": 0.5,
        "Water": 0.5
    },
    "Grass": {
        "Water": 2.0,
        "Rock": 2.0,
        "Fire": 0.5
    },
    "Electric": {
        "Water": 2.0,
        "Electric": 0.5,
        "Grass": 0.5,
        "Rock": 0.5
    },
    "Rock": {
        "Fire": 2.0,
        "Electric": 1.0,
        "Water": 1.0,
        "Grass": 1.0
    },
    "Normal": {
        "Rock": 0.5
    }
}


class Move:
    """
    Represents a Pokémon move.
    """

    def __init__(self, name, power, max_pp, type_="Normal"):
        self.name = name
        self.power = power
        self.max_pp = max_pp
        self.current_pp = max_pp
        self.type = type_

    def get_multiplier(self, defender_type):
        return TYPE_CHART.get(self.type, {}).get(defender_type, 1.0)

    def use_move(self):
        if self.current_pp > 0:
            self.current_pp -= 1
            return self.power
        return 0

    def __str__(self):
        return f"{self.name} ({self.type}, Power {self.power}, PP {self.current_pp}/{self.max_pp})"
