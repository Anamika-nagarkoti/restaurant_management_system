def validate_payment_choice(choice):

    if not choice.isdigit():
        return False

    if choice in ["1", "2", "3", "4"]:
        return True

    return False
