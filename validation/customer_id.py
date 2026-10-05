def validate_customer_id(user_id):
    return user_id.isdigit() and len(user_id) == 6