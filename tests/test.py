from strict_types import (
    ByteType,
    IntegerType,
    ShortType,
    PercentageType
)

byte = ByteType(-128)
short = ShortType(-9_000_000)
integer = IntegerType(-2_000_000_000)
percentage = PercentageType(75)

print(byte)
print(short)
print(integer)
print(percentage)
print(repr(percentage))