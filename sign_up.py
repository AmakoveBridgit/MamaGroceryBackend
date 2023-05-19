class Customer:
    def __init__(self, name, password, confirm_password, email):
        self.name = name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def sign_up(self):
        new_customer = Customer(self.name, self.password, self.confirm_password, self.email)
        return new_customer

new_customer = Customer("Emily Haile", "password22237828009", "haileemily@gmail.com")
print("You have signed up successfully")