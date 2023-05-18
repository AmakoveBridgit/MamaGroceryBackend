class Cart:
    def __init__(self):
        self.items=[]

    def add_Item(self,product,quantity):
        for item in self.items:
            if item['product']==product:
                item['quantity']+=quantity
                return
        self.items.append({'product':product,'quantity':quantity})
    def remove_item(self,product):
        for item in self.items:
            if item['product']==product:
                self.items.remove(item)

    def empty_cart(self):
        self.items=[]