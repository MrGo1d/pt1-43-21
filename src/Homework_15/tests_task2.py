"""
Module for testing task2 Homework_15
"""


import unittest
from unittest import TestCase
from ddt import ddt, data, unpack
from task2 import some_func


@ddt
class TestParametricDecorator(TestCase):
    """Test case for parametric decorator, that calls the function a certain number of times,
    if the function is executed without an exception, the decorator finishes work,
    upon expiration of attempts it raises an exception TooManyErrors.
    For correct testing please enter number for decorator calls more than 2"""

    @data((0, 'Error!'))
    @unpack
    def test_1(self, some_n, expected):
        """The first test throws an exception"""
        self.assertEqual(some_func(some_n), expected)

    @data((1, 1.0))
    @unpack
    def test_2(self, some_n, expected):
        """The second test get input values for test pass"""
        self.assertEqual(some_func(some_n), expected)

    @data((0, 'Error!'))
    @unpack
    def test_3(self, some_n, expected):
        """The third and subsequent tests will throw an exception"""
        self.assertRaises(SystemExit, some_func, some_n, expected)

    @data((1, 1.0))
    @unpack
    def test_4(self, some_n, expected):
        """The third and subsequent tests will throw an exception"""
        self.assertRaises(SystemExit, some_func, some_n, expected)


if __name__ == '__main__':
    unittest.main()