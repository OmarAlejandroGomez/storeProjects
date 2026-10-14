from models.item import Item
from models.product import Product

class ItemController:
    
    def __init__(self):
        self.items = []
    
    def add_item(self, name, description, price):
        item = Item(name, description, price)
        self.items.append(item)   

    def add_product(self, name, description, price):
        product = Product(name, description, price)
        self.items.append(product)
        
    def get_item(self):
        return self.items.copy()
    