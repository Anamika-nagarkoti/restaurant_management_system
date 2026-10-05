from validation.payment_validation import validate_payment_choice


def payment(total):

    print("==============================")
    print("          PAYMENT")
    print("==============================")

    print("Amount to Pay: ₹", total)

    print("1. Cash")
    print("2. UPI")
    print("3. Card")
    print("4. Back")

    choice = input("Enter payment method: ")

    if not validate_payment_choice(choice):
        print("Invalid payment choice")
        return

    if choice == "1":
        print("Payment successful!")
        print("Payment Method: Cash")

    elif choice == "2":
        print("Payment successful!")
        print("Payment Method: UPI")

    elif choice == "3":
        print("Payment successful!")
        print("Payment Method: Card")

    elif choice == "4":
        return

    print("Amount Paid: ₹", total)