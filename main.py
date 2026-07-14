# main.py
# Assignment 2 Bringing dictionaries and list together:
# Date: 07/03/2026
# Author: Casimiro Sigala
# Purpose: Build a simple inventory system for a small store. The inventory should be a dictionary where each key is a product name
# and each value is another dictionary containing the price and quantity of that product.

""" Write a program that lets the user do the following through a menu loop. 
 View all products with their price and quantity formatted cleanly.
 Add a new product with a price and quantitiy.
 Restock an existing product by adding to its quantity.
 Sell a product by reducing its quantity by 1 -- if the quantity hits 0 print a warning that the item is out of stock.
 Remove a product
 Add proper error handling incase the user enter a product name that doesn't exist. """

""" Update 07/04/2026 :
    Update new feature - Added file saving and loading to the inventory system """
import sys
# Update 07/04/2026: Added Pathlib import Path and import Json
from pathlib import Path

# Update 07/13/2024 import mudual file paths
from product import Product, NonPerishableProduct, PerishableProduct
from inventory_helpers import find_product, save_inventory, load_inventory, get_aisle, get_name, get_price, get_stock


# Update 07/13/2026 REFACTORING!
# removed dictionary
# Removed file load into dictionary
# Removed if dictionary not found use premade dictionary
# Added
# Added objects
# added file load function
# added if file not found use premade objects
# dictionary Update 07/13/2026: Removed empty dictionary repalced with empty list
inventory = []
# Update 07/04/2026: check if file inventory.Json exist if it does load inventory data into dictionary else load hardcoaded dictionary
inventory_file = Path('inventory.json')

# checks if inventory.Json is in path and if its a file returns bool
if inventory_file.is_file():
    # with statement so we dont forget to close, opens inventory.json and reads file. f is variable we use to refer to file now.
    inventory = load_inventory(inventory_file)
    
else:
    # dictionary to use if no file is found
    inventory = [
    NonPerishableProduct("Bat", 30.99, "T20", 4, 112),
    PerishableProduct("Apples", 1.50, "A1", 15, "07/22/2026"),
    NonPerishableProduct("Couch", 210.59, "H10", 3, 111)
    ]
# Functions:
# main menu
# Update - 07/05/ 2026 enter 0 now notifies user of file to be created
def display_menu():
    
    print('---------------------------------------------------------')
    print('|Enter 1 - View inventory                                |')
    print('|Enter 2 - Add a new product                             |')
    print('|Enter 3 - Restock an existing product                   |')
    print('|Enter 4 - Sell a product                                |')
    print('|Enter 5 - Remove a product                              |')
    print('|Enter 0 - To close program and create inventory file    |')
    print('---------------------------------------------------------')
    try:
        user_input = int(input())
        return user_input
    except ValueError:
        return None
# add a new product 
# Update 7/13/2026 - ask user what product they would like to make uses if statement to create either Product,NonPerishableProduct, or PerishableProduct object
def add_new_product():

    while True:
        try:
            print("1: Product\n2: Perishable Product\n3: Non Perishable Product")
            choice = int(input())
            if 1 <= choice <= 3:
                break
            print("Please enter 1, 2, or 3")
        except ValueError:
            print("Error: Please enter a valid integer")

    name = get_name()
    price = get_price()
    aisle = get_aisle()
    stock = get_stock()

    if choice == 1:
        inventory.append(Product(name, price, aisle, stock))

    elif choice == 2:
        expir_date = input("Please enter expiration date:")
        inventory.append(PerishableProduct(name, price, aisle, stock, expir_date))
    
    elif choice == 3:
        while True:
            try:
                upc = int(input("Please enter UPC: "))
                if upc > 0:
                    break
                print("Error: UPC must be positive")
            except ValueError:
                print("Error: Please enter a valid integer")
        inventory.append(NonPerishableProduct(name, price, aisle, stock, upc))
    
    print("Item successfully added!")
# Update 7/14/2026 - 
# Removed - restock from dictionary
# Added - get's object and  calls product.restock()

def restock_item():
    print('What item would you like to restock:')
    while True:
        try:
            user_input_name = input()
            product = find_product(inventory, user_input_name)

            user_input_restock = get_stock()
            try:
                # Restock the item
                print(product.restock(user_input_restock))
                break
            except ValueError as e:
                print(f"Error: {e}")
        except ValueError:
            print("Please enter a item in inventory")
              
# Sells one item prints warning if item == 0
# Update 7/13/2026 Removed dictionary sell item. Added class sell item
def sell_item():
    print('What item was bought?:')
    while True:
        try:
            user_input_name = input()
            product = find_product(inventory, user_input_name)
            print(product.sell())
            break
        except ValueError as e:
            print(f"Error: {e}")
    
# Remove a product from inventory
# Update 7/14/2026 removed dictionary product removal. Added - list product removal
def remove_product():
    print('What product would you like to remove?')
    while True:
        try:
            user_input_name = input()
            product = find_product(inventory, user_input_name)
            inventory.remove(product)
            print(f"The following was successfully removed: {product}")
            break
        except ValueError:
            print("Please enter an item in inventory")

# Menu loop
try:
    while True:
        user_input = display_menu()
        
# 1 == view all products with their price and quantity formated cleanly
        if user_input == 1:
            print('Inventory:')
            # use a for loop to iterate through every product, price, and stock
            # Update: 7/13/2026 - removed loop through dictionary - added loop through inventory list
            for product in inventory:
                print(product)
                        
            
# 2 == add a new product with a price and quantity
        elif user_input == 2:
            print('Add new product:')
            add_new_product()
            print('product added')

            
# 3 == restock an existing product by adding to its quantity
        elif user_input == 3:
            print('Restock item:')
            restock_item()

#4 == sell a product reduce its quantity by 1 - add if statement checking if product is at 0 and print warning if True
        elif user_input == 4:
            sell_item()
# 5 Remove a product
        elif user_input == 5:
            remove_product()
# Enter 0 to end program and write to file
        elif user_input == 0:
            # UPDATE - 7/05/2026: added dave dictionary to Json file and added print statement informing user of Json file creating.
            # UPDATE - 7/14/2026: removed save dictionary to json file and added function to that converts list objects to dictionary and stores them in JSON file
            try:
                save_inventory(inventory, inventory_file)
                print("Save Successful!")
                break
            except Exception as e:
                print(f"Error saving file: {e}")
        else:
            print('Please enter a valid menu option')
# add proper error handling
except KeyboardInterrupt:
    sys.exit()