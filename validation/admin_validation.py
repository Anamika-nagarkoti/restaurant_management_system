def validate_admin_choice(choice):

    if not choice.isdigit():
        return False

    if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return True

    return False


def validate_menu_choice(choice):

    if not choice.isdigit():
        return False

    if choice in ["1", "2"]:
        return True

    return False


def validate_table_choice(choice):

    if not choice.isdigit():
        return False

    if choice in ["1", "2", "3", "4"]:
        return True

    return False


def validate_user_choice(choice):

    if not choice.isdigit():
        return False

    if choice in ["1", "2"]:
        return True

    return False