from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id : str, name : str, price : float, stock : int, download_size : int, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfillment_info(self):
        return "this product is delivered digitally"