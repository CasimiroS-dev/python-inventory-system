# Assignment 2 Bringing dictionaries and list together:

# Build a simple inventory system for a small store. The inventory should be a dictionary where each key is a product name
# and each value is another dictionary containing the price and quantity of that product.

# Write a program that lets the user do the following through a menu loop. 
# View all products with their price and quantity formatted cleanly.
# Add a new product with a price and quantitiy.
# Restock an existing product by adding to its quantity.
# Sell a product by redicing its quantity by 1 -- if the quantity hits 0 print a warning that the item is out of stick.
# Remove a product
# Add proper error handling incase the user enter a product name that doesn't exist.

import sys

# dictionary
inventory = {
    'apples': {'price': 0.99, 'quantity': 50},
    'bread': {'price': 2.49, 'quantity': 20},
    'milk': {'price': 3.99, 'quantity': 15}
}

# Functions
# main menu
def display_menu():
    print('-------------------------------------------------')
    print('|Enter 1 - View inventory                       |')
    print('|Enter 2 - Add a new product                    |')
    print('|Enter 3 - Restock an existing product          |')
    print('|Enter 4 - Sell a product                       |')
    print('|Enter 5 - Remove a product                     |')
    print('|Enter 0 - To close program                     |')
    print('-------------------------------------------------')

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
# Enter 0 to end program
        elif user_input == 0:
            break
        else:
            print('Please enter a valid menu option')
# add proper error handling
except KeyboardInterrupt:
    sys.exit()