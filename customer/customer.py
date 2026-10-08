import json
from table.table import book_table, cancel_booking
from order.order_service import order_food, cancel_order
from validation.customer_validation import validate_customer_choice, validate_rating


def customer_menu():

    while True:

        print("=====================")
        print("    CUSTOMER MENU")
        print("=====================")

        print("1. Book Table")
        print("2. Cancel Table Booking")
        print("3. Order Food")
        print("4. Cancel Order")
        print("5. Give Rating & Feedback")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if not validate_customer_choice(choice):
            print("Invalid choice")
            continue

        if choice == "1":
            book_table()

        elif choice == "2":
            cancel_booking()

        elif choice == "3":
            order_food()

        elif choice == "4":
            cancel_order()

        elif choice == "5":
            give_feedback()

        elif choice == "6":
            print("Logout")
            break

        else:
            print("Invalid choice")


def give_feedback():

    rating = input("Enter your rating (1-5): ")

    if not validate_rating(rating):
        print("Invalid rating")
        return

    feedback = input("Enter your feedback: ")

    with open("database/feedback.json", "r") as file:
        feedbacks = json.load(file)

    new_feedback = {"user_id": "123456", "rating": int(rating), "feedback": feedback}

    feedbacks.append(new_feedback)

    with open("database/feedback.json", "w") as file:
        json.dump(feedbacks, file, indent=4)

    print("Feedback submitted successfully!")
