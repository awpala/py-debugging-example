import unittest
from unittest import mock
from io import StringIO

from file_manager import FileManager
from user import User

class FileManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_data.txt'
        self.file_manager = FileManager(self.filename)

    def tearDown(self):
        try:
            with open(self.filename, 'r') as file:
                file.close()
                # Remove the file after the test is complete
                # to ensure a clean environment for the next test
                import os
                os.remove(self.filename)
        except FileNotFoundError:
            pass

    def test_load_data_file_not_found(self):
        with mock.patch('builtins.open', side_effect=FileNotFoundError):
            with mock.patch('sys.stdout', new=StringIO()) as captured_output:
                users = self.file_manager.load_data()

        expected_output = f"{self.filename} not found. Starting with an empty database.\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
        self.assertEqual(users, [])

    def test_load_data_empty_file(self):
        with open(self.filename, 'w'):
            pass

        users = self.file_manager.load_data()
        self.assertEqual(users, [])

    def test_load_data_valid_file(self):
        users_data = [
            'John,25,john@example.com\n',
            'Alice,30,alice@example.com\n',
            'Bob,35,bob@example.com\n'
        ]
        expected_users = [
            User('John', 25, 'john@example.com'),
            User('Alice', 30, 'alice@example.com'),
            User('Bob', 35, 'bob@example.com')
        ]

        with open(self.filename, 'w') as file:
            file.writelines(users_data)

        users = self.file_manager.load_data()

        # Compare the attributes of the User objects
        for expected_user, actual_user in zip(expected_users, users):
            self.assertEqual(expected_user.name, actual_user.name)
            self.assertEqual(expected_user.age, actual_user.age)
            self.assertEqual(expected_user.email, actual_user.email)

    def test_save_data(self):
        users = [
            User('John', 25, 'john@example.com'),
            User('Alice', 30, 'alice@example.com'),
            User('Bob', 35, 'bob@example.com')
        ]

        with mock.patch('sys.stdout', new=StringIO()) as captured_output:
            self.file_manager.save_data(users)

        expected_output = f"Data saved to {self.filename}\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        with open(self.filename, 'r') as file:
            saved_data = file.readlines()

        expected_data = [
            'John,25,john@example.com\n',
            'Alice,30,alice@example.com\n',
            'Bob,35,bob@example.com\n'
        ]
        self.assertEqual(saved_data, expected_data)

if __name__ == '__main__':
    unittest.main()
