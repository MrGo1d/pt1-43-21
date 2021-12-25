"""
Module for testing task1 Homework_15
"""


import unittest
from unittest import TestCase
from ddt import ddt, data, unpack
import task1


@ddt
class TestClasses(TestCase):
    """Test case for task1"""
    @data((1, 1, 1, 1, 1), (2, 1, 3, 1, 1), (5, 5, 5, 1, 1))
    @unpack
    def test_1(self, health, attack, defend, experience, level):
        """The test check, that 'inst' is instance of class 'Hero'"""
        inst = task1.Hero(health, attack, defend, experience, level)
        self.assertIsInstance(inst, task1.Hero)

    @data((1, 1, 1, 1, 1), (1, 2, 3, 1, 1))
    @unpack
    def test_2(self, health, attack, defend, experience, level):
        """The test check, that 'inst' (instance of Enemy class) is not instance of class 'Hero'"""
        inst = task1.Enemy(health, attack, defend, experience, level)
        self.assertNotIsInstance(inst, task1.Hero)

    @data(('a', 1, 1, 1, 1), (1, 2, [], 'c', 1))
    @unpack
    def test_3(self, health, attack, defend, experience, level):
        """The test raises an exception when entering incorrect data"""
        with self.assertRaises(TypeError) as error:
            task1.Hero(health, attack, defend, experience, level)
            self.assertEqual('Incorrect input: characteristic must be a integer!', error.exception.args[0])

    @data((-1, 1, 1, 1, -1), (1, 1, -1, 1, 2))
    @unpack
    def test_4(self, health, attack, defend, experience, level):
        """The test raises an exception when entering negative number """
        with self.assertRaises(TypeError) as error:
            task1.Hero(health, attack, defend, experience, level)
            self.assertEqual("Characteristics can't be less than 0!", error.exception.args[0])


if __name__ == '__main__':
    unittest.main()