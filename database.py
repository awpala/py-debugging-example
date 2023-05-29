from user import User
from utils import get_input, validate_int

class Database:
    def __init__(self, users: list[User]):
        self.users = users

    def create_user(self):
        print("Create User")
        name = get_input("Enter name: ")
        age = validate_int("Enter age: ")
        email = get_input("Enter email: ")

        user = User(name, age, email)
        self.users.append(user)
        print("User created successfully.\n")

    def read_user(self):
        print("Read User")
        email = get_input("Enter email: ")

        user = self.find_user_by_email(email)
        if user:
            print(user)
        else:
            print("User not found.\n")

    def update_user(self):
        print("Update User")
        email = get_input("Enter email: ")

        user = self.find_user_by_email(email)
        if user:
            name = get_input("Enter new name: ")
            age = validate_int("Enter new age: ")

            user.name = name
            user.age = age
            print("User updated successfully.\n")
        else:
            print("User not found.\n")

    def delete_user(self):
        print("Delete User")
        email = get_input("Enter email: ")

        user = self.find_user_by_email(email)
        if user:
            self.users.remove(user)
            print("User deleted successfully.\n")
        else:
            print("User not found.\n")

    def find_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None
