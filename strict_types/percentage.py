from .base import BoundedInt

class PercentageType(BoundedInt):
    MIN = 0
    MAX = 100

    def __repr__(self):
        return f"{int(self)}%"