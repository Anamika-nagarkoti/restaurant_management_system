def validate_item_id(item_id, menu):

    if not item_id.isdigit():
        return False

    item_id = int(item_id)

    for item in menu:
        if item["id"] == item_id:
            return True

    return False


def validate_quantity(quantity):

    if not quantity.isdigit():
        return False

    if int(quantity) <= 0:
        return False

    return True