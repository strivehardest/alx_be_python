# File: fns_and_dsa/test_arithmetic_operations.py

import unittest
from arithmetic_operations import perform_operation

class TestPerformOperation(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(perform_operation(5, 3, 'add'), 8)

    def test_subtraction(self):
        self.assertEqual(perform_operation(10, 4, 'subtract'), 6)

    def test_multiplication(self):
        self.assertEqual(perform_operation(7, 6, 'multiply'), 42)

    def test_division(self):
        self.assertEqual(perform_operation(8, 2, 'divide'), 4.0)

    def test_division_by_zero(self):
        self.assertEqual(perform_operation(8, 0, 'divide'), "Error: Division by zero")

    def test_invalid_operation(self):
        self.assertEqual(perform_operation(5, 5, 'mod'), "Error: Invalid operation")

    def test_case_insensitivity(self):
        # This will fail unless the calling script normalizes the input,
        # because the function expects 'add', not 'Add' or 'ADD'.
        self.assertEqual(perform_operation(5, 3, 'Add'), "Error: Invalid operation")


if __name__ == '__main__':
    unittest.main()
