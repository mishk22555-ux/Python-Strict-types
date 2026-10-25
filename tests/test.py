import pytest

from strict_types import ByteType, IntegerType, PercentageType, ShortType


def test_byte():
    assert ByteType(127) == 127
    assert ByteType(-128) == -128

    with pytest.raises(ValueError):
        ByteType(128)


def test_short():
    assert ShortType(9_000_000) == 9_000_000

    with pytest.raises(ValueError):
        ShortType(9_000_001)


def test_integer():
    assert IntegerType(2_000_000_000) == 2_000_000_000

    with pytest.raises(ValueError):
        IntegerType(2_000_000_001)


def test_percentage():
    assert PercentageType(75) == 75

    with pytest.raises(ValueError):
        PercentageType(101)