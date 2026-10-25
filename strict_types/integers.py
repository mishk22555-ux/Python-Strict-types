from .base import BoundedInt

class ByteType(BoundedInt):
    MIN = -128
    MAX = 127


class ShortType(BoundedInt):
    MIN = -9_000_000
    MAX = 9_000_000


class IntegerType(BoundedInt):
    MIN = -2_000_000_000
    MAX = 2_000_000_000