class User:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"
