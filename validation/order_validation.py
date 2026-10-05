def validate_quantity(quantity):

    if not quantity.isdigit():
        return False

    if int(quantity) <= 0:
        return False

    return True