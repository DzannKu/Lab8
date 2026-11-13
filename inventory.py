from product import Product

class Inventory:
    def __init__(self):
        self.products : list[Product] = []


    def add_product(self, product : Product):
        self.products.append(product)

    def search_product(self, product_id : str):
        for item in self.products:
            if item._Product__product_id == product_id:
                return item

        return None

    def remove_product(self, product_id : str):
        for item in self.products:
            if item._Product__product_id == product_id:
                print(f"Product found: {item._Product__name} (ID: {item._Product__product_id})")
                print("Would you like to remove this product from the inventory? (y/n)")
                choice = input().lower()
                if choice == 'y':
                    self.products.remove(item)
                    return True
                
        return False

    def display_all(self):
        print("Current Inventory")
        print("------------------------------")

        for product in self.products:
            product.display_information()

        print("------------------------------")
        print("")

    
