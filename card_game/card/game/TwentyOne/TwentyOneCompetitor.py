import random
from card_game.Player import Player

class TwentyOneCompetitor(Player):

    def __init__(self, competitor_type, name: str, level_of_risk: int = 0):
        super().__init__(competitor_type, name)
        if level_of_risk == 0:
            self.level_of_risk = 11 + random.randint(0, 7)
        else:
            self.level_of_risk = level_of_risk

    def get_level_of_risk(self) -> int:
        return self.level_of_risk