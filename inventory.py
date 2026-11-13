class Inventory:
    def __init__(self):
        self.products = []


    def add_product(self, product):
        self.products.append(product)

    def search_product(self, productID):
        for item in self.products:
            if item._Product__product_id == productID:
                return item

        return None

    def display_all(self):
        print("Current Inventory")
        print("------------------------------")

        for product in self.products:
            product.display_information()

        print("------------------------------")
        print("")

    
