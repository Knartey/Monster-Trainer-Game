# battle.py
import random

class Battle:
    def __init__(self, player, monster1, monster2):
        self.player = player
        self.monster1 = monster1
        self.monster2 = monster2

    def start(self):
        print(f"\nBattle: {self.monster1.name} vs {self.monster2.name}!")
        while not self.monster1.is_fainted() and not self.monster2.is_fainted():
            self.take_turn(self.monster1, self.monster2)
            if self.monster2.is_fainted():
                print(f"{self.monster2.name} fainted! {self.monster1.name} wins!")
                break
            self.take_turn(self.monster2, self.monster1)
            if self.monster1.is_fainted():
                print(f"{self.monster1.name} fainted! {self.monster2.name} wins!")
                break

    def take_turn(self, attacker, defender):
        """Each monster picks a move and attacks."""
        available_moves = [move for move in attacker.moves if move.pp > 0]
        if not available_moves:
            print(f"{attacker.name} has no moves left!")
            return
        move = random.choice(available_moves)
        move.use(attacker, defender)
