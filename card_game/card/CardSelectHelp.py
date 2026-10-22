from enum import Enum

class CardSelectHelp(Enum):
    DISCARD = "Pick from discarded pile"
    DECK = "Pick from Deck"

    def __str__(self):
        return self.value