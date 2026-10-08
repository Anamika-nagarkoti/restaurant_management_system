import json
from billing.payment import payment


def generate_bill():

    with open("database/order.json", "r") as file:
        orders = json.load(file)

    if not orders:
        print("No orders available.")
        return

    print("==============================")
    print("      RESTAURANT BILL")
    print("==============================")

    total = 0

    for order in orders:

        amount = order["price"] * order["quantity"]

        print(
            order["item"],
            "Qty:", order["quantity"],
            "Price:", order["price"],
            "Amount:", amount
        )

        total = total + amount

    print("------------------------------")
    print("Total:", total)
    print("==============================")

    payment(total)

    # Payment ke baad purane orders clear
    with open("database/order.json", "w") as file:
        json.dump([], file)

    print("Order cleared successfully.")