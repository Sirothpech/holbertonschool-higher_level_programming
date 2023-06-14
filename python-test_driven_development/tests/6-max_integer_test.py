#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -5, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 3, -5, 0]), 3)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_list(self):
        self.assertEqual(max_integer([1.2, 4.1, 3.6, 2.2]), 4.1)

    def test_isnone(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'a', 4, 5])


if __name__ == "__main__":
    unittest.main()
