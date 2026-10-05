import json

from validation.user_id import validate_user_id
from validation.staff_id import validate_staff_id
from validation.customer_id import validate_customer_id
from validation.password import validate_password


def signin():

    print("=====================")
    print("SIGNIN")
    print("=====================")

    user_id = input("enter your id: ")
    password = input("enter your password: ")

    if not validate_password(password):
        print("Invalid password")
        return None

    if validate_user_id(user_id):
        print("Admin ID")

    elif validate_staff_id(user_id):
        print("Staff ID")

    elif validate_customer_id(user_id):
        print("Customer ID")

    else:
        print("Invalid ID")
        return None

    with open("database/user.json", "r") as file:
        users = json.load(file)

    for user in users:

        if user["user_id"] == user_id and user["password"] == password:
            print("Login successful!")
            print("Role:", user["role"])
            return user["role"]

    print("Invalid ID or password")
    return None