from inventory import Inventory
from product import Product
import json
from digitalproduct import DigitalProduct
from physicalproduct import PhysicalProduct
from supplier import Supplier

def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            print("inventory.json found.")

            data = json.load(file)

            for item in data:
                if item["type"] == "physical":
                    product = PhysicalProduct(
                        item["product_id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["weight"]
                    )

                elif item["type"] == "digital":
                    product = DigitalProduct(
                        item["product_id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["download_size"]
                    )

                inventory.add_product(product)

            print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("Inventory file not found. Starting with empty inventory.")

    return inventory

def save_inventory(inventory):
    data = []

    for product in inventory.products:

        if isinstance(product, PhysicalProduct):
            data.append({
                "type": "physical",
                "product_id": product._Product__product_id,
                "name": product._Product__name,
                "price": product._Product__price,
                "stock": product._Product__stock,
                "weight": product._PhysicalProduct__weight
            })

        elif isinstance(product, DigitalProduct):
            data.append({
                "type": "digital",
                "product_id": product._Product__product_id,
                "name": product._Product__name,
                "price": product._Product__price,
                "stock": product._Product__stock,
                "download_size": product._DigitalProduct__download_size
            })

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully!")
    
def exit_program(inventory):
    print("Saving inventory before exiting...")
    save_inventory(inventory)

    print("")
    print("Thank you for using the Inventory Management System")
    print("Program terminated.")

#Main code here

def user_menu(inventory):
        print("------------ MENU ------------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("------------------------------")
        while True:
            print("")
            user_option = input("Enter option: ")
            print("")
            if user_option == "1":
                inventory.display_all()
                continue
            
            if user_option == "2":
                input_type = input("Enter product type (digital/physical): ").lower()
                if input_type == "digital":
                    product_id = input("Enter product ID: ")
                    name = input("Enter product name: ")
                    price = float(input("Enter product price: "))
                    stock = int(input("Enter product stock: "))
                    download_size = float(input("Enter download size (in MB): "))
                    digital_product = DigitalProduct(product_id, name, price, stock, download_size)
                    inventory.add_product(digital_product)
                    print("")
                    print("Digital product added successfully!")
                    
                elif input_type == "physical":
                    product_id = input("Enter product ID: ")
                    name = input("Enter product name: ")
                    price = float(input("Enter product price: "))
                    stock = int(input("Enter product stock: "))
                    weight = float(input("Enter weight (in kg): "))
                    physical_product = PhysicalProduct(product_id, name, price, stock, weight)
                    inventory.add_product(physical_product)
                    print("")
                    print("Physical product added successfully!")
                else:
                    print("Invalid product type. Please enter 'digital' or 'physical'.")

            if user_option == "3":
                print("Update Stock")
                product_id = input("Enter product ID: ")
                print("")
                product = inventory.search_product(product_id)

                if product:
                    print("Product found!")
                    print(f"Name: {product._Product__name}")
                    print(f"Current Stock: {product._Product__stock}")
                    print("")
                    quantity = int(input("Enter new stock quantity: "))
                    product.update_stock(quantity)
                    print("")
                    print("Stock updated successfully!")
                else:
                    print("Product Not Found")

            if user_option == "4":
                product_id = input("Enter product ID: ")
                searched_product = inventory.search_product(product_id)
                print("")
            
                if searched_product:
                    print("Product found!")
                    print("-------------------------------")
                    searched_product.display_information()
                    print("-------------------------------")
                else:
                    print("Product Not Found")

            if user_option == "5":
                save_inventory(inventory)
                continue
            
            if user_option == "6":
                exit_program(inventory)
                break

def main():
    inventory = load_inventory()
    user_menu(inventory)

main()
