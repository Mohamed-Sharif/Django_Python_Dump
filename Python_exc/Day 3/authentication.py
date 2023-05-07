import re
import os
import getpass

USER_DATA_FILE = "users.txt"

def validate_email(email):
    """
    Validates the email format.
    """
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email)

def validate_phone(phone):
    """
    Validates the phone number format.
    """
    pattern = r"^01[0-2]\d{8}$"
    return re.match(pattern, phone)

def register():
    """
    Registers a new user.
    """
    print("Registration:")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    while not validate_email(email):
        print("Invalid email format.")
        email = input("Email: ")
    password = getpass.getpass("Password: ")
    confirm_password = getpass.getpass("Confirm password: ")
    while password != confirm_password:
        print("Passwords do not match.")
        password = getpass.getpass("Password: ")
        confirm_password = getpass.getpass("Confirm password: ")
    phone = input("Mobile phone: ")
    while not validate_phone(phone):
        print("Invalid phone number format.")
        phone = input("Mobile phone: ")

    # Append the user data to the file.
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{email},{password},{first_name},{last_name},{phone}\n")
    print("Registration successful.")

def login(email, password):
    """
    Logs in an existing user.
    """
    print("Login:")

    # Check if the email and password match.
    with open(USER_DATA_FILE, "r") as f:
        for line in f:
            line = line.strip().split(",")
            if line[0] == email and line[1] == password:
                print("Login successful.")
                return True
    print("Invalid email or password.")
    return False
