from product import Product
from canbeshipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id : str, name : str, price : float, stock : int, weight : float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfillment_info(self):
        return "this product requires physical shipping"

    def calculate_shipping_cost(self):
        weight_cost = 5.0  #cost per kg 
        shipping_cost = self.__weight * weight_cost
        return shipping_cost
