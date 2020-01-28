from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):
    def test_add_numbers(self):
        """tests that numbers are added together"""
        self.assertEqual(add(9, 4), 13)
    
    def test_subtract_numbers(self):
        self.assertEqual(subtract(2,5), -3)