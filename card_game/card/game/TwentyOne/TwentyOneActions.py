from enum import Enum

class TwentyOneActions(Enum):
    TWIST = 0
    STICK = 1
    
    def __init__(self, num):
        self.num = num
    
    def values():
        return [action.value for action in TwentyOneActions]

