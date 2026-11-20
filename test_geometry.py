import math
import unittest

import circle
import square


# Values are calculated from the geometric formulas independently of the code.
CIRCLE_CASES = (
    (0, 0, 0),
    (0.0, 0, 0),
    (-0.0, 0, 0),
    (1, 3.141592653589793, 6.283185307179586),
    (2, 12.566370614359172, 12.566370614359172),
    (5, 78.53981633974483, 31.41592653589793),
    (0.5, 0.7853981633974483, 3.141592653589793),
    (0.1, 0.03141592653589793, 0.6283185307179586),
    (1.25, 4.908738521234052, 7.853981633974483),
    (3.5, 38.48451000647497, 21.99114857512855),
    (1e-9, 3.141592653589793e-18, 6.283185307179586e-9),
    (10**9, 3.141592653589793e18, 6.283185307179586e9),
)

SQUARE_CASES = (
    (0, 0, 0),
    (0.0, 0, 0),
    (-0.0, 0, 0),
    (1, 1, 4),
    (2, 4, 8),
    (5, 25, 20),
    (0.5, 0.25, 2),
    (0.1, 0.01, 0.4),
    (1.25, 1.5625, 5),
    (3.5, 12.25, 14),
    (1e-9, 1e-18, 4e-9),
    (10**9, 10**18, 4 * 10**9),
)


class GeometryTestCase(unittest.TestCase):
    def assert_result(self, actual, expected):
        if isinstance(expected, int):
            self.assertEqual(actual, expected)
        else:
            self.assertTrue(
                math.isclose(actual, expected, rel_tol=1e-12, abs_tol=0.0),
                f"expected {expected!r}, got {actual!r}",
            )

    def assert_invalid_calls(self, function):
        invalid_calls = (((), {}), ((2, 3), {}), ((), {"value": 2}), ((None,), {}))
        for args, kwargs in invalid_calls:
            with self.subTest(function=function.__name__, args=args, kwargs=kwargs):
                with self.assertRaises(TypeError):
                    function(*args, **kwargs)


class CircleTestCase(GeometryTestCase):
    def test_area(self):
        for radius, expected, _ in CIRCLE_CASES:
            with self.subTest(radius=radius):
                self.assert_result(circle.area(radius), expected)

    def test_perimeter(self):
        for radius, _, expected in CIRCLE_CASES:
            with self.subTest(radius=radius):
                self.assert_result(circle.perimeter(radius), expected)

    def test_area_invalid_calls(self):
        self.assert_invalid_calls(circle.area)

    def test_perimeter_invalid_calls(self):
        self.assert_invalid_calls(circle.perimeter)

    def test_area_scales_quadratically(self):
        self.assert_result(circle.area(6), 9 * circle.area(2))

    def test_perimeter_scales_linearly(self):
        self.assert_result(circle.perimeter(6), 3 * circle.perimeter(2))


class SquareTestCase(GeometryTestCase):
    def test_area(self):
        for side, expected, _ in SQUARE_CASES:
            with self.subTest(side=side):
                self.assert_result(square.area(side), expected)

    def test_perimeter(self):
        for side, _, expected in SQUARE_CASES:
            with self.subTest(side=side):
                self.assert_result(square.perimeter(side), expected)

    def test_area_invalid_calls(self):
        self.assert_invalid_calls(square.area)

    def test_perimeter_invalid_calls(self):
        self.assert_invalid_calls(square.perimeter)

    def test_area_scales_quadratically(self):
        self.assertEqual(square.area(6), 9 * square.area(2))

    def test_perimeter_scales_linearly(self):
        self.assertEqual(square.perimeter(6), 3 * square.perimeter(2))
