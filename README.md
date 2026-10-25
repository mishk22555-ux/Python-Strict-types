# Python Strict Types

A lightweight Python library that provides strict numeric types with explicit value boundaries and runtime validation.

## Features

- Strict integer types with defined minimum and maximum values.
- Automatic validation when creating instances.
- Clear exceptions for invalid values.
- No runtime dependencies.
- Type annotations and PEP 561 support.
- Compatible with Python 3.10+.

## Clone the repository

```bash
git clone git@github.com:mishk22555-ux/Python-Strict-types.git
```

## Installation
```bash
pip install strict-types
```

## Available Types

| Type | Minimum | Maximum |
|---|---:|---:|
| `ByteType` | -128 | 127 |
| `ShortType` | -9,000,000 | 9,000,000 |
| `IntegerType` | -2,000,000,000 | 2,000,000,000 |
| `PercentageType` | 0 | 100 |

All numeric types currently accept integers only.

## Usage

### Integer Types

```python
from strict_types import ByteType, ShortType, IntegerType

byte = ByteType(127)
short = ShortType(5_000_000)
integer = IntegerType(1_500_000_000)

print(byte)
print(short)
print(integer)
```

### PercentageType

```python
from strict_types import PercentageType

percentage = PercentageType(75)

print(percentage)        # 75
print(repr(percentage))  # 75%
```

### Runtime Validation

Values outside the supported range raise a `ValueError`.

```python
from strict_types import ByteType

byte = ByteType(200)  # Raises ValueError
```

Non-integer values raise a `TypeError`.

```python
byte = ByteType("100")  # Raises TypeError
```

### Arithmetic Operations

Numeric types inherit from Python's built-in `int`.

```python
from strict_types import ByteType

a = ByteType(100)
b = ByteType(50)

result = a + b

print(result)        # 150
print(type(result))  # <class 'int'>
```

Arithmetic operations currently return regular Python integers, so range validation is not automatically applied to arithmetic results.

## Development

Install development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run tests:

```bash
python -m pytest
```

Check code quality:

```bash
ruff check .
mypy strict_types
```

Build the package:

```bash
python -m build
```

## Project Structure

```text
Python-Strict-types/
├── strict_types/
│   ├── __init__.py
│   ├── base.py
│   ├── integers.py
│   ├── percentage.py
│   └── py.typed
├── tests/
│   └── test.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0-only).

See the [LICENSE](LICENSE) file for the full license text.

Copyright (C) 2026 Mikhail.

## Author

**Mikhail**

GitHub: https://github.com/mishk22555-ux/Python-Strict-types