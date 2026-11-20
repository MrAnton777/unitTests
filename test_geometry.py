import unittest

import circle
import square


class CircleTestCase(unittest.TestCase):
    def test_01_area(self):
        self.assertAlmostEqual(circle.area(2), 12.5663706144)

    def test_02_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_03_area_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.area(-1)

    def test_04_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(2), 12.5663706144)

    def test_05_perimeter_fractional_radius(self):
        self.assertAlmostEqual(circle.perimeter(0.5), 3.1415926536)

    def test_06_perimeter_none(self):
        with self.assertRaises(TypeError):
            circle.perimeter(None)


class SquareTestCase(unittest.TestCase):
    def test_07_area(self):
        self.assertEqual(square.area(5), 25)

    def test_08_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_09_area_fractional_side(self):
        self.assertEqual(square.area(0.5), 0.25)

    def test_10_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_11_perimeter_fractional_side(self):
        self.assertEqual(square.perimeter(0.5), 2)

    def test_12_perimeter_string(self):
        with self.assertRaises(TypeError):
            square.perimeter("2")
