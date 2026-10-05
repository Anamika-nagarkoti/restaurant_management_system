import json
from validation.table_validation import validate_table_ids


def book_table():

    with open("database/tables.json", "r") as file:
        tables = json.load(file)

    table_id = input("Enter Table ID: ")

    for table in tables:

        if str(table["id"]) == table_id:

            if table["status"] == "Available":

                print("Table Type:", table["type"])
                print("Seats:", table["seats"])

                booking_date = input("Enter booking date:")
                booking_time = input("Enter booking time:")

                table["status"] = "Booked"
                table["booking_date"] = booking_date
                table["booking_time"] = booking_time

                with open("database/tables.json", "w") as file:
                    json.dump(tables, file, indent=4)

                print("Table booked successfully!")
                return

            else:
                print("Table is already booked")
                return

    print("Invalid Table ID")

def cancel_booking():

    with open("database/tables.json", "r") as file:
        tables = json.load(file)

    table_id = input("Enter Table ID: ")

    for table in tables:

        if str(table["id"]) == table_id:

            if table["status"] == "Booked":

                table["status"] = "Available"

                if "booking_date" in table:
                    del table["booking_date"]

                if "booking_time" in table:
                    del table["booking_time"]

                with open("database/tables.json", "w") as file:
                    json.dump(tables, file, indent=4)

                print("Booking cancelled successfully!")
                return

            else:
                print("Table is not booked")
                return

    print("Invalid Table ID")