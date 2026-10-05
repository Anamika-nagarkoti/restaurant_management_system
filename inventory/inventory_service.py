import json


def inventory_menu():

    while True:

        print("=====================")
        print("      INVENTORY")
        print("=====================")

        print("1. View Inventory")
        print("2. Add Stock")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            add_stock()

        elif choice == "3":
            break

        else:
            print("Invalid choice")


def view_inventory():

    with open("database/inventory.json", "r") as file:
        inventory = json.load(file)

    print("=====================")
    print("      INVENTORY")
    print("=====================")

    for item in inventory:

        print("ID:", item["id"])
        print("Item:", item["item"])
        print("Stock:", item["stock"])
        print("---------------------")


def add_stock():

    item_name = input("Enter item name: ")
    stock = int(input("Enter stock: "))

    with open("database/inventory.json", "r") as file:
        inventory = json.load(file)

    new_id = len(inventory) + 1

    inventory.append({
        "id": new_id,
        "item": item_name,
        "stock": stock
    })

    with open("database/inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Stock added successfully!")