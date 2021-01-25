from django.test import TestCase

from .calc import add, subtract


class CalcTests(TestCase):

    def test_add_two_numbers(self):
        """test that two numbers are added"""
        self.assertEqual(add(5, 9), 14)

    def test_subtract_numbers(self):
        """test that two numbers are subtracted from each other and returned"""
        self.assertEqual(subtract(8, 4), 4)
