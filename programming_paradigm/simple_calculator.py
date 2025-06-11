import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtract(self):
        """Test subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(3.5, 1.5), 2.0)

    def test_multiply(self):
        """Test multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_divide(self):
        """Test division method."""
        self.assertEqual(self.calc.divide(6, 2), 3.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 2), -3.0)
        self.assertEqual(self.calc.divide(-6, -2), 3.0)
        self.assertIsNone(self.calc.divide(5, 0))  # Edge case: division by zero

    def test_divide_by_zero(self):
        """Specifically test division by zero."""
        self.assertIsNone(self
