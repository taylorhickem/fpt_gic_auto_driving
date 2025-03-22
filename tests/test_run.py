"""unit tests to verify working as expected
"""
import unittest
from crash import drive


class CrashTests(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(drive.add(2, 3), 5)


if __name__ == '__main__':
    unittest.main()
