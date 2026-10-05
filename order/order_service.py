import json
from validation.item import validate_item_id
from validation.order_validation import validate_quantity


def order_food():

    print("=====================")
    print("      FOOD MENU")
    print("=====================")

    with open("database/menu.json", "r") as file:
        menu = json.load(file)

    for item in menu:
        print(item["id"], ".", item["name"], "- ₹", item["price"])

    
    item_ids = input("Enter item IDs (comma separated): ")

    ids = item_ids.split(",")

    orders = []

    for item_id in ids:

        item_id = item_id.strip()

        if not item_id.isdigit():
            print("Invalid item ID:", item_id)
            continue

        item_id = int(item_id)

        selected_item = None

        for item in menu:
            if item["id"] == item_id:
                selected_item = item
                break

        if selected_item is None:
            print("Invalid item ID:", item_id)
            continue

        quantity = input(
            "Enter quantity for " + selected_item["name"] + ": "
        )

        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid quantity")
            continue

        quantity = int(quantity)

        amount = selected_item["price"] * quantity

        orders.append({
            "item": selected_item["name"],
            "quantity": quantity,
            "price": selected_item["price"],
            "total": amount
        })

    if not orders:
        print("No item ordered.")
        return


    with open("database/order.json", "r") as file:
        old_orders = json.load(file)

    old_orders.extend(orders)

    with open("database/order.json", "w") as file:
        json.dump(old_orders, file, indent=4)

    
    total = 0

    print("=====================")
    print("ORDER SUCCESSFULLY!")
    print("=====================")

    for order in orders:

        print(
            order["item"],
            "Qty:", order["quantity"],
            "Price:", order["price"],
            "Amount:", order["total"]
        )

        total += order["total"]

    print("---------------------")
    print("TOTAL: ₹", total)
    print("=====================")

