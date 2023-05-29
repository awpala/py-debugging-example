def get_input(prompt):
    return input(prompt).strip()

def validate_int(prompt):
    while True:
        value = get_input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter a valid integer.")
