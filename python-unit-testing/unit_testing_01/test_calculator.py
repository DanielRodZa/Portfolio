import unittest
import calculator as calculator


class TestsCalculator(unittest.TestCase):
    def test_add_functionality(self):
        result = calculator.calc_add(10, 20)
        self.assertEqual(result, 30)

    def test_add_functionality_two_negative_numbers(self):
        result = calculator.calc_add(-10, -20)
        self.assertEqual(result, -30)


class TestsCalculator_3(unittest.TestCase):
    def test_add_functionality(self):
        result = calculator.calc_add(50, 20)
        self.assertEqual(result, 70)

    def test_add_functionality_two_negative_numbers(self):
        result = calculator.calc_add(-10, -50)
        self.assertEqual(result, -60)

    def test_add_functionality_one_negative_number(self):
        result = calculator.calc_add(-10, 40)
        self.assertEqual(result, 30)

class TestsCalculator2(unittest.TestCase):
    def test_add_functionality2(self):
        result = calculator.calc_add(10, 20)
        self.assertEqual(result, 30)

    def test_add_functionality_two_negative_numbers2(self):
        result = calculator.calc_add(-10, -20)
        self.assertEqual(result, -30)
