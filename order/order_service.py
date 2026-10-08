import json


def order_food():

    print("══════════════════════════════════════")
    print("            FOOD MENU                 ")
    print("══════════════════════════════════════")

    with open("database/menu.json", "r") as file:
        menu = json.load(file)

    categories = [
        "Starter",
        "Chinese",
        "Main Course",
        "Biryani",
        "Fast Food",
        "Drinks"
    ]

    for category in categories:

        print("            " + category.upper())
        print("────────────────────────────────────────")

        for item in menu:

            if item["category"] == category:

                if "half_price" in item:

                    print(
                        item["id"],
                        ".",
                        item["name"],
                        "  H ₹",
                        item["half_price"],
                        "| F ₹",
                        item["full_price"]
                    )

                else:

                    print(
                        item["id"],
                        ".",
                        item["name"],
                        "  ₹",
                        item["price"]
                    )

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

        if "half_price" in selected_item:

            size = input(
                "Select size for "
                + selected_item["name"]
                + " (H/F): "
            ).upper()

            if size not in ["H", "F"]:
                print("Invalid size")
                continue

            if size == "H":
                price = selected_item["half_price"]
                size_name = "Half"
            else:
                price = selected_item["full_price"]
                size_name = "Full"

        else:

            price = selected_item["price"]
            size_name = ""

        quantity = input(
            "Enter quantity for "
            + selected_item["name"]
            + ": "
        )

        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid quantity")
            continue

        quantity = int(quantity)

        amount = price * quantity

        orders.append({
            "item": selected_item["name"],
            "size": size_name,
            "quantity": quantity,
            "price": price,
            "total": amount
        })

    if not orders:
        print("No item ordered.")
        return

    try:
        with open("database/order.json", "r") as file:
            old_orders = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        old_orders = []

    old_orders.extend(orders)

    with open("database/order.json", "w") as file:
        json.dump(old_orders, file, indent=4)

    total = 0

    print("=====================")
    print("ORDER SUCCESSFULLY!")
    print("=====================")

    for order in orders:

        if order["size"]:

            print(
                order["item"],
                "(" + order["size"] + ")",
                "Qty:", order["quantity"],
                "Price:", order["price"],
                "Amount:", order["total"]
            )

        else:

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


def cancel_order():

    try:
        with open("database/order.json", "r") as file:
            orders = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("No orders found.")
        return

    if not orders:
        print("No orders found.")
        return

    print("=====================")
    print("     YOUR ORDERS")
    print("=====================")

    for i, order in enumerate(orders, start=1):

        if order.get("size"):

            print(
                i,
                ".",
                order["item"],
                "(" + order["size"] + ")",
                "Qty:",
                order["quantity"],
                "Amount:",
                order["total"]
            )

        else:

            print(
                i,
                ".",
                order["item"],
                "Qty:",
                order["quantity"],
                "Amount:",
                order["total"]
            )

    choice = input("Enter order number to cancel: ")

    if not choice.isdigit():
        print("Invalid order number")
        return

    choice = int(choice)

    if choice < 1 or choice > len(orders):
        print("Invalid order number")
        return

    cancelled_order = orders.pop(choice - 1)

    with open("database/order.json", "w") as file:
        json.dump(orders, file, indent=4)

    print(
        cancelled_order["item"],
        "cancelled successfully!"
    )