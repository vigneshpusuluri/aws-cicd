import unittest

from Calculator import add, subtract, multiply, divide


class BasicCalculatorTest(unittest.TestCase):

    def test_add(self):
        result = add(2, 2)
        self.assertEqual(4, result)

    def test_subtract(self):
        result = subtract(4, 2)
        self.assertEqual(2, result)

    def test_multiply(self):
        result = multiply(4, 2)
        self.assertEqual(8, result)

    def test_divide(self):
        result = divide(4, 2)
        self.assertEqual(2, result)

if __name__ == '__main__':
    unittest.main()