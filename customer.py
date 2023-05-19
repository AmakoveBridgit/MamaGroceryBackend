

class Customer:
    def __init__(self, name, customer_id,email):
     self.name = name
     self.id = customer_id
     self.email = email

    def add_customer(self, customer):
        if customer.id in self.customers:
            return False
        self.customers[customer.id] = customer
        return True

customers=Customer()
customer1=Customer(1,"Peter","peter@gmail.com")
customer2=Customer(2,"Alice","alice@gmail.com")

customers.add_customer(customer1)
customers.add_product(customer2)



def check_customer(self, customer_id):
        if customer_id in self.customers:
            return self.customers[customer_id]
        return None

customer_id =1
customer= customers.check_customer(customer_id)
if customer:
    print(f"Customer found - ID: {customer.id}, Name: {customer.name}, Email: {customer.email}")
else:
    print(f"Customer with ID {customer_id} not found.")


    

 

