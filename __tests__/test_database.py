import unittest
from unittest import mock
from io import StringIO
from database import Database
from user import User

class DatabaseTestCase(unittest.TestCase):
    @mock.patch('database.get_input')
    @mock.patch('database.validate_int')
    def test_create_user(self, mock_validate_int: mock.Mock, mock_get_input: mock.Mock):
        mock_get_input.side_effect = ['John', 'john@example.com']
        mock_validate_int.return_value = 25

        db = Database([])
        db.create_user()

        mock_get_input.assert_has_calls([
            mock.call('Enter name: '),
            mock.call('Enter email: ')
        ])
        mock_validate_int.assert_called_once_with('Enter age: ')

        self.assertEqual(len(db.users), 1)
        self.assertEqual(db.users[0].name, 'John')
        self.assertEqual(db.users[0].age, 25)
        self.assertEqual(db.users[0].email, 'john@example.com')

    @mock.patch('database.get_input')
    def test_read_user_found(self, mock_get_input: mock.Mock):
        email = 'john@example.com'
        user = User('John', 25, email)
        db = Database([user])

        mock_get_input.return_value = email

        with mock.patch('sys.stdout', new=StringIO()) as captured_output:
            db.read_user()

        expected_output = f'Read User\n{str(user)}\n\n'
        self.assertEqual(captured_output.getvalue(), expected_output)

    @mock.patch('database.get_input')
    def test_read_user_not_found(self, mock_get_input: mock.Mock):
        email = 'john@example.com'
        db = Database([])

        mock_get_input.return_value = email

        with mock.patch('sys.stdout', new=StringIO()) as captured_output:
            db.read_user()

        expected_output = 'Read User\nUser not found.\n\n'
        self.assertEqual(captured_output.getvalue(), expected_output)

    @mock.patch('database.get_input')
    def test_update_user_not_found(self, mock_get_input: mock.Mock):
        email = 'john@example.com'
        db = Database([])

        mock_get_input.return_value = email

        with mock.patch('sys.stdout', new=StringIO()) as captured_output:
            db.update_user()

        expected_output = 'Update User\nUser not found.\n\n'
        self.assertEqual(captured_output.getvalue(), expected_output)

    @mock.patch('database.get_input')
    def test_delete_user_found(self, mock_get_input: mock.Mock):
        email = 'john@example.com'
        user = User('John', 25, email)
        db = Database([user])

        mock_get_input.return_value = email

        with mock.patch('sys.stdout', new=StringIO()) as captured_output:
            db.delete_user()

        self.assertEqual(len(db.users), 0)

        expected_output = 'Delete User\nUser deleted successfully.\n\n'
        self.assertEqual(captured_output.getvalue(), expected_output)

    @mock.patch('database.get_input')
    def test_delete_user_not_found(self, mock_get_input: mock.Mock):
        email = 'john@example.com'
        db = Database([])

        mock_get_input.return_value = email

        with mock.patch('sys.stdout', new=StringIO()) as captured_output:
            db.delete_user()

        expected_output = 'Delete User\nUser not found.\n\n'
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
