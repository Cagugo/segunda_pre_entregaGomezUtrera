class Customer:
    def __init__(self, name, email, address, phone_number):
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Address: {self.address}, Phone Number: {self.phone_number}"
