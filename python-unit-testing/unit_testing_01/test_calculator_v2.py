import unittest
from calculator_v2 import Calculator


class TestsCalculatorV2(unittest.TestCase):
    def test_add_functionality(self):
        calc1 = Calculator(10, 30)
        result = calc1.calc_add()
        self.assertEqual(result, 40)

    def test_add_functionality_with_one_negative_number(self):
        calc1 = Calculator(10, -30)
        result = calc1.calc_add()
        self.assertEqual(result, -20)


class TestsCalculatorV2_2(unittest.TestCase):
    def test_add_functionality(self):
        calc = Calculator(10, 30)
        result = calc.calc_add()
        self.assertEqual(result, 40)

