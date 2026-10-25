class BoundedInt(int):
    MIN = None
    MAX = None

    def __new__(cls, value: int):
        if type(value) is not int:
            raise TypeError("Value must be an integer")

        if not cls.MIN <= value <= cls.MAX:
            raise ValueError(
                f"{cls.__name__} must be between "
                f"{cls.MIN} and {cls.MAX}"
            )

        return super().__new__(cls, value)