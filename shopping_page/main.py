import json
from shopping_page.customer import Customer

def register_customer(customers):
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    address = input("Enter customer address: ")
    phone_number = input("Enter customer phone number: ")

    new_customer = Customer(name, email, address, phone_number)
    customers[name] = new_customer

    return "Customer registered successfully."

def show_information(customers):
    if customers:
        return "\nInformation of registered customers:\n" + "\n".join(str(customer) for customer in customers.values())
    else:
        return "No customers registered yet."

def login_customer(customers):
    name = input("Enter your name: ")
    if name in customers:
        return "Login successful."
    else:
        return "Customer not found."

def main():
    try:
        with open('customers.json', 'r') as file:
            customers_data = json.load(file)
            customers = {name: Customer(**data) for name, data in customers_data.items()}
    except FileNotFoundError:
        customers = {}

    while True:
        print("\nOptions:")
        print("1. Register customer")
        print("2. Show information")
        print("3. Login")
        print("4. Exit")

        option = input("Choose an option (1-4): ")

        if option == '1':
            print(register_customer(customers))
        elif option == '2':
            print(show_information(customers))
        elif option == '3':
            print(login_customer(customers))
        elif option == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

    with open('customers.json', 'w') as file:
        customers_data = {name: vars(customer) for name, customer in customers.items()}
        json.dump(customers_data, file, indent=4)

if __name__ == "__main__":
    main()
