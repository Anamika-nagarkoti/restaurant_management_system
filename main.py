from authentication.signin import signin
from admin.admin import admin_menu
from staff.staff import staff_menu
from customer.customer import customer_menu

print("=============================")
print("RESTAURANT MANAGEMENT SYSTEM")
print("==============================")


print("1.signin")
print("2.exit")

choice = input("enter your choice:")

if choice == "1":
    role = signin()

    if role == "admin":
        admin_menu()

    elif role == "staff":
        staff_menu()

    elif role == "customer":
        customer_menu()


elif choice == "2":
    exit()
