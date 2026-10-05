import json

from table.table import book_table, cancel_booking
from inventory.inventory_service import inventory_menu
from order.order_service import order_food
from billing.billing_service import generate_bill

from validation.admin_validation import (
    validate_admin_choice,
    validate_menu_choice,
    validate_table_choice,
    validate_user_choice
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
        print("6. Reports")
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
              reports()

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

        if not validate_menu_choice(choice):
         print("Invalid choice")
         continue

        if choice == "1":

            with open("database/menu.json", "r") as file:
                menu = json.load(file)

            print("=====================")
            print("        MENU")
            print("=====================")

            for item in menu:
                print("ID:", item["id"])
                print("Name:", item["name"])
                print("Category:", item["category"])
                print("Price:", item["price"])
                print("---------------------")

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
        print("2. Back")

        choice = input("Enter your choice: ")
        
        if not validate_user_choice(choice):
         print("Invalid choice")
         continue


        if choice == "1":

            with open("database/user.json", "r") as file:
                users = json.load(file)

            print("=====================")
            print("       USERS")
            print("=====================")

            for user in users:
                print("ID:", user["user_id"])
                print("Role:", user["role"])
                print("---------------------")

        elif choice == "2":
            break

        else:
            print("Invalid choice")


      


def reports():

    with open("database/order.json", "r") as file:
        orders = json.load(file)

    total_orders = len(orders)
    total_sales = 0

    for order in orders:
        total_sales = total_sales + (order["price"] * order["quantity"])

    print("==============================")
    print("          REPORTS")
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