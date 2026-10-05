import json
from table.table import book_table, cancel_booking

def place_order():

    with open("database/menu.json", "r") as file:
        menu = json.load(file)

    print("=====================")
    print("        MENU")
    print("=====================")

    for item in menu:
        print(item["id"], item["name"], "-", item["price"])

    choice = input("Enter dish ID: ")
    quantity = input("Enter quantity: ")

    for item in menu:

        if str(item["id"]) == choice:

            order = {
                "item": item["name"],
                "price": item["price"],
                "quantity": int(quantity)
            }

            with open("database/order.json", "r") as file:
                orders = json.load(file)

            orders.append(order)

            with open("database/order.json", "w") as file:
                json.dump(orders, file, indent=4)

            print("Order placed successfully!")
            return

    print("Invalid dish ID")




def staff_menu():

  while True:

    print("=====================")
    print("      STAFF MENU")
    print("=====================")

    print("1. Manage Orders")
    print("2. Manage Tables")
    print("3. Billing")
    print("4. Logout")

    choice = input("Enter your choice: ")

    if choice == "1":
        place_order()

    elif choice == "2":
        manage_tables()

    elif choice == "3":
        generate_bill()

    elif choice == "4":
        print("Logout")
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

        else:
            print("Invalid choice")

def generate_bill():

    with open("database/order.json", "r") as file:
        orders = json.load(file)

    print("==============================")
    print("      RESTAURANT BILL")
    print("==============================")

    total = 0

    for order in orders:

        amount = order["price"] * order["quantity"]

        print(
            order["item"],
            "Qty:", order["quantity"],
            "Price:", order["price"],
            "Amount:", amount
        )

        total = total + amount

    print("------------------------------")
    print("Total:", total)
    print("==============================")

