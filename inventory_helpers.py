import json
from product import Product, NonPerishableProduct, PerishableProduct
# inventory_helpers.py
# Created 07/12/2026
# Author: Casimiro Sigala
# Purpose: contains helper functions not tied to class

# add find_product() function loops through the inventory list and returns the matching product object or None if not found 
def find_product(inventory, name):
    for product in inventory:
        if product.name == name:
            return product    
    raise ValueError("Product not found")

#add save_inventory function loops through the inventory list, calls to_dict() on each object, and writes the resulting list to a JSON file
def save_inventory(inventory, filepath):

    with open(filepath, 'w', encoding='UTF-8') as f:
        json.dump([product.to_dict() for product in inventory], f, indent=4)

        
        




# add load_inventory function that reads the JSON file, checks the type key on each dictionary, and rebuilds the right class for each entry
def load_inventory(filepath):

    inventory = []

    with open(filepath, 'r', encoding='UTF-8') as f:
        data = json.load(f)
        for product in data:
            if product.get('type') == 'Product':
                inventory.append(Product(product.get('name'), product.get('price'), product.get('aisle'), product.get('stock')))
            elif product.get('type') == 'NonPerishableProduct':
                inventory.append(NonPerishableProduct(product.get('name'), product.get('price'), product.get('aisle'), product.get('stock'), product.get('UPC')))
            elif product.get('type') == 'PerishableProduct':
                inventory.append(PerishableProduct(product.get('name'), product.get('price'), product.get('aisle'), product.get('stock'), product.get('expir_date')))
    

    return inventory
# get functions for attibutes of Product Object and subclasses
def get_name():
    while True:
        name = input("Please enter product name: ").strip()
        if name:
            return name
        print("Error: Name cannont be empty")
def get_price():
    while True:
        try:
            price = float(input("Please enter price: "))
            if price >= 0:
                return price
            print("Error: Price must be positive")
        except ValueError:
            print("Error: Please enter a valid number")
def get_stock():
    while True:
        try:
            stock = int(input("Please enter stock: "))
            if stock >= 0:
                return stock
            print("Error: Stock cannot be negative")
        except ValueError:
            print("Error: Please enter a valid integer")
def get_aisle():
    while True:
        aisle = input("Please enter aisle location: ").strip()
        if aisle:
            return aisle
        print("Error: Aisle cannot be empty")
            

