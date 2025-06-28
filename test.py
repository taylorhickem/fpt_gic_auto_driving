"""unit tests to verify working as expected
"""
import unittest
from crash import drive


class CrashTests(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(drive.add(2, 3), 5)

    def test_grid_create_fail_empty(self):
        expected = -1
        response_actual = drive.grid_create()
        actual = response_actual.get('success')
        self.assertEqual(expected, actual)

    def test_grid_create_fail_non_integer(self):
        expected = -1
        response_actual = drive.grid_create(h='h', w=3)
        actual = response_actual.get('success')
        self.assertEqual(expected, actual)

    def test_grid_create_fail_negative_integer(self):
        expected = -1
        response_actual = drive.grid_create(h=-1, w=3)
        actual = response_actual.get('success')
        self.assertEqual(expected, actual)

    def test_grid_create_success(self):
        expected = 1
        response_actual = drive.grid_create(h=1, w=3)
        actual = response_actual.get('success')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
