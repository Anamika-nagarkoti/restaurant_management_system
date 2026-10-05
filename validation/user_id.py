def validate_user_id(user_id):

    if user_id.isdigit() and len(user_id) == 4:
        return True

    return False