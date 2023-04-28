from app import calc
from django.test import SimpleTestCase


class CalcTest(SimpleTestCase):

    def test_add_two(self):

        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subctracting numbers """
        res = calc.subtract(15, 10)

        self.assertEqual(res, 5)


