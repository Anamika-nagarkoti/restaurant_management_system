
import json


def book_table():

    with open("database/tables.json", "r") as file:
        tables = json.load(file)

    print("=====================")
    print("      BOOK TABLE")
    print("=====================")

    booking_date = input("Enter booking date: ")
    booking_time = input("Enter booking time: ")

    people = int(input("Enter number of people: "))

    print("\n1. Normal")
    print("2. VIP")

    table_choice = input("Enter table type: ")

    if table_choice == "1":
        table_type = "Normal"

    elif table_choice == "2":
        table_type = "VIP"

    else:
        print("Invalid table type")
        return

    # Find suitable available table
    for table in tables:

        if (
            table["status"] == "Available"
            and table["type"] == table_type
            and table["seats"] >= people
        ):

            table_id = table["id"]

            # Read existing bookings
            try:
                with open("database/bookings.json", "r") as file:
                    bookings = json.load(file)
            except FileNotFoundError:
                bookings = []

            # Check whether this table is already booked
            # for the selected date and time
            already_booked = False

            for booking in bookings:

                if (
                    booking["table_id"] == table_id
                    and booking["date"] == booking_date
                    and booking["time"] == booking_time
                    and booking["status"] == "Booked"
                ):
                    already_booked = True
                    break

            if already_booked:
                continue

            # Create booking ID
            booking_id = "B" + str(len(bookings) + 1).zfill(3)

            customer_id = input("Enter customer ID: ")

            new_booking = {
                "booking_id": booking_id,
                "customer_id": customer_id,
                "date": booking_date,
                "time": booking_time,
                "people": people,
                "type": table_type,
                "table_id": table_id,
                "status": "Booked"
            }

            bookings.append(new_booking)

            with open("database/bookings.json", "w") as file:
                json.dump(bookings, file, indent=4)

            print("\nTable booked successfully!")
            print("Booking ID:", booking_id)
            print("Table ID:", table_id)
            print("Table Type:", table_type)
            print("Seats:", table["seats"])
            print("Date:", booking_date)
            print("Time:", booking_time)
            print("People:", people)

            return

    print("\nNo suitable table available for the selected date and time.")


def cancel_booking():

    with open("database/bookings.json", "r") as file:
        bookings = json.load(file)

    booking_id = input("Enter Booking ID: ")

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            if booking["status"] == "Booked":

                booking["status"] = "Cancelled"

                with open("database/bookings.json", "w") as file:
                    json.dump(bookings, file, indent=4)

                print("Booking cancelled successfully!")
                return

            else:
                print("Booking is already cancelled")
                return

    print("Invalid Booking ID")


def view_table_status():

    with open("database/tables.json", "r") as file:
        tables = json.load(file)

    with open("database/bookings.json", "r") as file:
        bookings = json.load(file)

    booked_table_ids = []

    for booking in bookings:

        if booking["status"] == "Booked":
            booked_table_ids.append(booking["table_id"])

    total_tables = len(tables)
    booked_tables = len(set(booked_table_ids))
    available_tables = total_tables - booked_tables

    print("==============================")
    print("        TABLE STATUS")
    print("==============================")

    print("Total Tables     :", total_tables)
    print("Booked Tables    :", booked_tables)
    print("Available Tables :", available_tables)

    print("------------------------------")

    for table in tables:

        if table["id"] in booked_table_ids:
            status = "Booked"
        else:
            status = "Available"

        print(
            "Table", table["id"],
            "|", table["type"],
            "|", table["seats"], "Seats",
            "|", status
        )

