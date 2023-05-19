class Customer:
    def __init__(self, name, create_password, confirm_password, email):
        self.name = name
        self.email = email
        self.create_password = create_password
        self.confirm_password = confirm_password

    def sign_up(self,name,create_password,confirm_password,email):
        # new_customer = Customer(self.name, self.password, self.confirm_password, self.email)
        # return new_customer
       
        if self.name ==name and self.create_password == create_password and self.confirm_password==confirm_password and self.email==email:
            return " You have successfully signed up"

        else:
            return "You are require dto fill in the spaces"

new_customer = Customer("Emily Haile", "passwordI22j78", "passwordI22j78" ,"haileemily@gmail.com")
print("You have signed up successfully")