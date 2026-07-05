# Assignment 2 Bringing dictionaries and list together:
# Date: 07/03/2026:
# Build a simple inventory system for a small store. The inventory should be a dictionary where each key is a product name
# and each value is another dictionary containing the price and quantity of that product.

""" Write a program that lets the user do the following through a menu loop. 
 View all products with their price and quantity formatted cleanly.
 Add a new product with a price and quantitiy.
 Restock an existing product by adding to its quantity.
 Sell a product by redicing its quantity by 1 -- if the quantity hits 0 print a warning that the item is out of stick.
 Remove a product
 Add proper error handling incase the user enter a product name that doesn't exist. """

""" Update 07/04/2026 :
    Update new feature - Added file saving and loading to the inventory system """
import sys
# Update 07/04/2026: Added Pathlib import Path and import Json
from pathlib import Path
import json


# dictionary Update 07/04/2026: added empty dictionary so check if file inventory.Json works with no issue.
inventory = {}
# Update 07/04/2026: check if file inventory.Json exist if it does load inventory data into dictionary else load hardcoaded dictionary
inventory_file = Path('inventory.json')

# checks if inventory.Json is in path and if its a file returns bool
if inventory_file.is_file():
    # with statement so we dont forget to close, opens inventory.json and reads file. f is variable we use to refer to file now.
    with open(inventory_file, 'r', encoding='UTF-8') as f:
        # Json file returns dictionary
        inventory = json.load(f)
    
else:
    # dictionary to use if no file is found
    inventory = {
        'apples': {'price': 0.99, 'quantity': 50},
        'bread': {'price': 2.49, 'quantity': 20},
        'milk': {'price': 3.99, 'quantity': 15}
}

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

    user_input = int(input())
    return user_input
# add a new product
def add_new_product():
    print('Please enter product name:')
    new_product_name = input()
    print('Please enter product price:')
    new_product_price = float(input())
    print('Please enter product stock')
    new_product_stock = int(input())
    inventory.update({new_product_name: {'price': new_product_price, 'quantity': new_product_stock}})
# restock entered amount of items to user defined product
def restock_item():
    print('What item would you like to restock:')
    while True:
        user_input = input()

        if user_input in inventory:

            print(f'how much do you want to add to the existing inventory: ')
            additional_inventory = int(input())
            nested_dictionary = inventory.get(user_input)
            # get original quanitity from the nested dictionary
            original_inventory = nested_dictionary.get('quantity')
            new_inventory_amount = additional_inventory + original_inventory
        
            nested_dictionary['quantity'] = new_inventory_amount
            break
        else:
            print('Please enter an existing product to restock')
# Sells one item prints warning if item == 0
def sell_item():
    print('What item was bought?:')
    while True:
        user_input = input()

        if user_input in inventory:
            nested_dictionary = inventory.get(user_input)
            nested_dictionary['quantity'] -= 1
            if nested_dictionary['quantity'] == 0:
                print('Warning inventory is critically low please restock')
                break

            else:
                print(f'Inventory updated current inventory for {user_input} - {nested_dictionary.get('quantity')}')
                break

        else:
            print('Please enter an existing product to sell')

# Remove a product from inventory
def remove_product():
    print('What product would you like to remove?')
    while True:
        user_input = input()
        if user_input in inventory:
            removed_items = inventory.pop(user_input)
            print(f'The following has been removed {user_input} - {removed_items}')
            break
        else:
            print('please enter an existing product to remove')



# Menu loop
try:
    while True:
        user_input = display_menu()
        
# 1 == view all products with their price and quantity formated cleanly
        if user_input == 1:
            print('Inventory:')
            # use a for loop to iterate through every product, price, and stock
            for k,v in inventory.items():
                print(f"produce: {k} price: {v.get('price')} stock: {v.get('quantity')}")
            
            # use a for loop to iterate through every product, price, and stock
            
            
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
            try:
                with open(inventory_file, 'w', encoding='UTF-8') as f:
                    # writes dictionary into file added indentation for file readability
                    json.dump(inventory, f, indent=4)
                print(f'{inventory_file} file successfully updated! Have a great day!')
            except Exception as e:
                # notify of error and print error
                print(f'Error saving file: {e}')
            break
        else:
            print('Please enter a valid menu option')
# add proper error handling
except KeyboardInterrupt:
    sys.exit()