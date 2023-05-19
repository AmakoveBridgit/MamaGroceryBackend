class Customer:
    def __init__(self, name, password, confirm_password, email):
        self.name = name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def sign_up(self,name,password,confirm_password,email):
        # new_customer = Customer(self.name, self.password, self.confirm_password, self.email)
        # return new_customer
       
        if self.name ==name and self.password == password and self.confirm_password==confirm_password and self.email==email:
            return " You have successfully signed up"

        else:
            return "You are require dto fill in the spaces"

new_customer = Customer("Emily Haile", "password22237828009", "password22237828009" ,"haileemily@gmail.com")
print("You have signed up successfully")