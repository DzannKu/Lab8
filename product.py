from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):

    def __init__(self, product_id : str, name : str, price : float, stock : int, supplier: Supplier):
        self.__name = name
        self.__product_id = product_id
        self.__price = price
        self.__stock = stock
        self.supplier: Supplier = supplier

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price} | Stock: {self.__stock}")

    @abstractmethod
    def get_fulfillment_info(self):
        pass