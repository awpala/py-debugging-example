import unittest
from unittest import mock
from utils import get_input, validate_int

class UtilsTestCase(unittest.TestCase):
    class EndOfInput(Exception):
        pass

    @mock.patch('builtins.input')
    def test_get_input(self, mock_input: mock.Mock):
        mock_input.return_value = "test"
        self.assertEqual(get_input("Enter a value: "), "test")

    @mock.patch('builtins.input')
    def test_validate_int(self, mock_input: mock.Mock):
        mock_input.side_effect = self.generate_input(["10"])
        self.assertEqual(validate_int("Enter an integer: "), 10)

    @mock.patch('builtins.input')
    def test_validate_int_invalid(self, mock_input: mock.Mock):
        mock_input.side_effect = self.generate_input(["abc", "3.14", "10a"])
        with self.assertRaises(StopIteration):
            validate_int("Enter an integer: ")

    @staticmethod
    def generate_input(values: list[str | EndOfInput]):
        it = iter(values)
        while True:
            try:
                value = next(it)
                if isinstance(value, UtilsTestCase.EndOfInput):
                    raise value
                yield value
            except StopIteration:
                return

if __name__ == "__main__":
    unittest.main()
