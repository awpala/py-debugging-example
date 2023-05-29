from user import User

class FileManager:
    def __init__(self, filename: str):
        self.filename = filename

    def load_data(self):
        users: list[User] = []

        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    name, age, email = line.strip().split(",")
                    user = User(name, int(age), email)
                    users.append(user)
        except FileNotFoundError:
            print(f"{self.filename} not found. Starting with an empty database.")
        
        return users

    def save_data(self, users: list[User]):
        with open(self.filename, "w") as file:
            for user in users:
                file.write(f"{user.name},{user.age},{user.email}\n")
        print(f"Data saved to {self.filename}")
