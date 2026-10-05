def validate_table_ids(table_id):

    if not table_id.isdigit():
        return False

    if table_id in ["1", "2", "3", "4", "5"]:
        return True

    return False