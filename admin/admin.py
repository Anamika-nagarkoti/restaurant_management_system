import json
from datetime import date

from table.table import book_table, cancel_booking
from inventory.inventory_service import inventory_menu
from order.order_service import order_food
from billing.billing_service import generate_bill

from validation.admin_validation import (
    validate_admin_choice,
    validate_table_choice,
)


def admin_menu():

    while True:

        print("=====================")
        print("      ADMIN MENU")
        print("=====================")

        print("1. Manage Users")
        print("2. Manage Menu")
        print("3. Manage Tables")
        print("4. Manage Orders")
        print("5. Billing")
        print("6. Sales & Orders")
        print("7. Inventory")
        print("8. View Feedback")
        print("9. Logout")

        choice = input("Enter your choice: ")

        if not validate_admin_choice(choice):
            print("Invalid choice")
            continue

        if choice == "1":
            manage_users()

        elif choice == "2":
            manage_menu()

        elif choice == "3":
            manage_tables()

        elif choice == "4":
            order_food()

        elif choice == "5":
            generate_bill()

        elif choice == "6":
            sales_and_orders()

        elif choice == "7":
            inventory_menu()

        elif choice == "8":
            view_feedback()

        elif choice == "9":
            print("Logout")
            break

        else:
            print("Invalid choice")


def manage_menu():

    while True:

        print("=====================")
        print("     MANAGE MENU")
        print("=====================")

        print("1. View Menu")
        print("2. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            with open("database/menu.json", "r") as file:
                menu = json.load(file)

            print("================================================================")
            print("                         MENU")
            print("================================================================")

            print(f"{'ID':<5}" f"{'NAME':<30}" f"{'CATEGORY':<18}" f"{'PRICE':<10}")

            print("----------------------------------------------------------------")

            for item in menu:

                print(
                    f"{item['id']:<5}"
                    f"{item['name']:<30}"
                    f"{item['category']:<18}"
                    f"₹{item['price']:<9}"
                )

            print("================================================================")

        elif choice == "2":

            break

        else:

            print("Invalid choice")


def manage_tables():

    while True:

        print("=====================")
        print("    MANAGE TABLES")
        print("=====================")

        print("1. View Tables")
        print("2. Book Table")
        print("3. Cancel Booking")
        print("4. Back")

        choice = input("Enter your choice: ")

        if not validate_table_choice(choice):
            print("Invalid choice")
            continue

        if choice == "1":

            with open("database/tables.json", "r") as file:
                tables = json.load(file)

            print("=====================")
            print("       TABLES")
            print("=====================")

            for table in tables:
                print("Table ID:", table["id"])
                print("Seats:", table["seats"])
                print("Type:", table["type"])
                print("Status:", table["status"])

                if "booking_date" in table:
                    print("Date:", table["booking_date"])
                    print("Time:", table["booking_time"])

                print("---------------------")

        elif choice == "2":
            book_table()

        elif choice == "3":
            cancel_booking()

        elif choice == "4":
            break


def manage_users():

    while True:

        print("=====================")
        print("    MANAGE USERS")
        print("=====================")

        print("1. View Users")
        print("2. Add Staff")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice not in ["1", "2", "3"]:
            print("Invalid choice")
            continue

        if choice == "1":

            with open("database/user.json", "r") as file:
                users = json.load(file)

            print("================================================")
            print("                    USERS")
            print("================================================")
            print(
                f"{'ID':<15}"
                f"{'ROLE':<15}"
                f"{'PASSWORD':<15}"
                f"{'JOINING DATE':<15}"
            )

            print("------------------------------------------------")

            for user in users:

                print(
                    f"{user['user_id']:<15}"
                    f"{user['role']:<15}"
                    f"{'*' * len(user['password']):<15}"
                    f"{user.get('joining_date', '-'):<15}"
                )

            print("------------------------------------------------")

        elif choice == "2":

            print("=====================")
            print("       ADD STAFF")
            print("=====================")

            staff_id = input("Enter staff ID (10 digits): ")

            if not staff_id.isdigit() or len(staff_id) != 10:
                print("Invalid Staff ID")
                continue

            password = input("Enter staff password: ")

            if not password:
                print("Invalid password")
                continue

            with open("database/user.json", "r") as file:
                users = json.load(file)

            staff_exists = False

            for user in users:
                if user["user_id"] == staff_id:
                    staff_exists = True
                    break

            if staff_exists:
                print("Staff ID already exists")
                continue

            new_staff = {
                "user_id": staff_id,
                "password": password,
                "role": "staff",
                "joining_date": str(date.today()),
            }

            users.append(new_staff)

            with open("database/user.json", "w") as file:
                json.dump(users, file, indent=4)

            print("Staff added successfully!")

        elif choice == "3":
            break


def sales_and_orders():

    with open("database/order.json", "r") as file:
        orders = json.load(file)

    total_orders = len(orders)
    total_sales = 0

    for order in orders:
        total_sales = total_sales + (order["price"] * order["quantity"])

    print("==============================")
    print("   SALES & ORDERS")
    print("==============================")
    print("Total Orders:", total_orders)
    print("Total Sales:", total_sales)
    print("==============================")


def view_feedback():

    with open("database/feedback.json", "r") as file:
        feedbacks = json.load(file)

    print("=====================")
    print("      FEEDBACK")
    print("=====================")

    if not feedbacks:
        print("No feedback available.")

    else:
        for feedback in feedbacks:
            print("User ID:", feedback["user_id"])
            print("Rating:", feedback["rating"])
            print("Feedback:", feedback["feedback"])
            print("---------------------")
