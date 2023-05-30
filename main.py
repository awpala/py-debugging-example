import sys
from database import Database
from file_manager import FileManager

REQUIRED_ARGS_COUNT = 1

def main():
    if len(sys.argv) != REQUIRED_ARGS_COUNT + 1:
        print("Please provide a command line argument for the data file.")
        print("Usage: python main.py <data_file>")
        sys.exit(1)

    data_file = sys.argv[1]
    file_manager = FileManager(data_file)
    database = Database(file_manager.load_data())

    while True:
        print("1. Create User")
        print("2. Read User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            database.create_user()
        elif choice == "2":
            database.read_user()
        elif choice == "3":
            database.update_user()
        elif choice == "4":
            database.delete_user()
        elif choice == "5":
            file_manager.save_data(database.users)
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
