from enum import Enum

class YesOrNo(Enum):
    YES = 1
    NO = 2

    def __str__(self):
        return self.name