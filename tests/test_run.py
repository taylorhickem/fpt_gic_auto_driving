"""unit tests to verify working as expected
"""
import unittest
from crash import drive
from crash.ui import InteractiveApp


class CrashTests(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(drive.add(2, 3), 5)


class TestInteractiveApp(unittest.TestCase):
    def test_name_and_exit(self):
        inputs = iter(["Alice", "n"])
        outputs = []

        def mock_input(prompt):
            outputs.append(prompt)
            return next(inputs)

        def mock_output(message):
            outputs.append(message)

        app = InteractiveApp(input_fn=mock_input, output_fn=mock_output)
        app.run()

        expected = [
            "Enter your name: ",
            "Hello, Alice!",
            "Do you want to continue? (y/n): ",
            "Goodbye!"
        ]
        self.assertEqual(outputs, expected)


if __name__ == '__main__':
    unittest.main()
