import unittest
from code.calculations import Calculations


class TestCalculations(unittest.TestCase):
    def test_get_sum(self):
        calc = Calculations(10, 5)
        self.assertEqual(calc.get_sum(), 15)

    def test_get_difference(self):
        calc = Calculations(10, 5)
        self.assertEqual(calc.get_difference(), 5)

    def test_get_product(self):
        calc = Calculations(10, 5)
        self.assertEqual(calc.get_product(), 50)

    def test_get_quotient(self):
        calc = Calculations(10, 5)
        self.assertEqual(calc.get_quotient(), 2)


if __name__ == '__main__':
    unittest.main()
