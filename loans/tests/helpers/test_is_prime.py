from django.test import TestCase

from loans.helpers import is_prime

from parameterized import parameterized


# Create your tests here.

class IsPrimeTestCase(TestCase):
    @parameterized.expand([
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (7, True),
        (9, False),
        (11, True),
        (15, False),
        (27, False),
        (2017, True),
        (2117, False)
    ])
    def test_is_prime_with_positive_integer(self, number, expected_result):
        actual_result = is_prime(number)
        self.assertEqual(expected_result, actual_result)
        
