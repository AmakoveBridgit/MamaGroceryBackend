class Product:
    def __init__(self,name,price,description):
        self.name=name
        self.price=price
        self.description =description
    def Order(self,items):
        self.items = items
        self.total_price = sum([item['product'].price * item['quantity'] for item in items])
        print(f"Order")

items = [{'product': Product('Product1', 10, 'Description1'), 'quantity': 2},
         {'product': Product('Product2', 20, 'Description2'), 'quantity': 3}]

product = Product('Product3', 30, 'Description3')
product.Order(items)


# >>> from MamaGroceryBackend.product import Product
# >>> order=sum([400*2,300*3])
# >>> order
# 1700
# >>> 

# >>> from MamaGroceryBackend.product import Product
# >>> product1=("mango",233,"it is sweeter")
# >>> product1
# ('mango', 233, 'it is sweeter')
# >>> exit()
        
       
    
