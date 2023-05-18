class Items_on_offer:
    def __init__(self, item_name, price, items_on_offer, add_to_cart):
        self.item_name = item_name
        self.price = price
        self.items_on_offer ={}
        self.add_to_cart={}
    def check_offers_available(self):
        if self.item_name in self.items_on_offer.keys():
            self.add_to_cart[self.item_name] = self.price
        return self.add_to_cart
offer_items_in_store= Items_on_offer("Oranges", 300, {"Pineaples":200, "Mangoes":200 }, {})

print(offer_items_in_store.check_offers_available())