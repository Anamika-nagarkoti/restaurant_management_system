def validate_customer_choice(choice):

    if not choice.isdigit():
        return False

    if choice in ["1", "2", "3", "4"]:
        return True

    return False


def validate_rating(rating):

    if not rating.isdigit():
        return False

    rating = int(rating)

    if rating < 1 or rating > 5:
        return False

    return True