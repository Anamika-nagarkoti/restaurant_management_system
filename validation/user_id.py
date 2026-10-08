def validate_user_id(user_id):

    if not user_id.isdigit():
        return False

    if len(user_id) != 4:
        return False

    return True