# Geometric lib

A small Python library for calculating the area and perimeter of geometric shapes.

## Features
- Circle — area and perimeter
- Square — area and perimeter

### `circle.py`

| Function | Description | Example |
|---|---|---|
| `area(r)` | Returns the area of a circle with radius `r` | `print(area(5))` |
| `perimeter(r)` | Returns the perimeter of a circle with radius `r` | `print(perimeter(5))`|

### `square.py`

| Function | Description | Example |
|---|---|---|
| `area(a)` | Returns the area of a square with side `a` | `print(area(5))` |
| `perimeter(a)` | Returns the perimeter of a square with side `a` | `print(perimeter(5))` |

## Project Structure

```
unitTests/
├── circle.py   # circle area and perimeter
├── square.py   # square area and perimeter
├── test_geometry.py  # unit tests
└── docs/             # README and test report
```

## Commit history

| Commit hash | Message|
|---|---|
| ece58be | Added description for each function|
| 43aef4e | Updated README.md|

## Unit tests

Run from the repository root:

```sh
python3 -m unittest -v
```

See the [lab 4 test report](Test-Report.md) for the test plan, reproducible
cases, and results.

| Date | Change |
|---|---|
| 2026-11-20 | Added `test_geometry.py` with unit tests for circle and square. |
