# product.py
# Created 07/12/2026
# Author: Casimiro Sigala
# Purpose: contains Product, PerishableProduct, and NonPerishableProduct classes and

class Product:

    def __init__(self, name, price, aisle, stock):
        self.name = name
        self.price = price
        self.aisle = aisle
        self.stock = stock
    # self.__class__.__name__ allows us to get the class name
    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self._price}, '{self._aisle}', {self._stock})"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self._name} Price: ${self._price:.2f} Aisle: {self._aisle}, Stock: {self._stock}"
    
    # returns a clean dictionary of product
    def to_dict(self):
        return {
            'type': self.__class__.__name__,
            'name': self._name,
            'price': self._price,
            'aisle': self._aisle,
            'stock': self._stock
        }
    def sell(self):
        if self._stock == 0:
            raise ValueError("Out of stock!")
        self._stock -= 1
        if self._stock == 0:
            return f"Warning: {self._name} is now out of stock!"
        return f"{self._name} sold! Remaining stock: {self._stock}"
    
    def restock(self, quantity):
        if quantity <= 0:
            raise ValueError("Restock quantity must be a positive number")
        self._stock += quantity
        return f"{self._name} restocked! New stock: {self._stock}"
    
    
        
    # getters for product attibutes
    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    @property
    def aisle(self):
        return self._aisle
    @property
    def stock(self):
        return self._stock
    
    # setters for product attibutes
    @name.setter
    def name(self, new_name):
        # this checks if the string is empty by removing all spaces if it is raise value error
        if not new_name.strip():
            raise ValueError("Please enter a valid name")
        self._name = new_name
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price must be at least $0")
        self._price = new_price
    @aisle.setter
    def aisle(self, new_aisle):
        if not new_aisle.strip():
            raise ValueError("Please enter a valid location")
        self._aisle = new_aisle
    @stock.setter
    def stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("Please enter a valid integer")
        self._stock = new_stock
    
    
# Create sub classes NonPerishableProduct and PerishableProduct
class NonPerishableProduct(Product):
    def __init__(self, name, price, aisle, stock, upc):
        super().__init__(name, price, aisle, stock)

        self.upc = upc
    #TODO: ADD repr
    def __str__(self):
        return f"{super().__str__()} UPC: {self._upc}"
    
    def to_dict(self):
        # ** unpacks all key value pairs from parent into a new dictionary
        return {**super().to_dict() , 'UPC': self._upc}


    @property
    def upc(self):
        return self._upc
    @upc.setter
    def upc(self, new_upc):
        if new_upc < 0:
            raise ValueError("Please enter a valid integer")
        self._upc = new_upc
    # TODO: later add adding a validator that checks for UPC's that match each other We can also do the same thing with name if we get specific with the name IE: Cereal: Kellong, Captain Crunch, Fruit loops. 


class PerishableProduct(Product):
    def __init__(self, name, price, aisle, stock, expir_date):
        super().__init__(name, price, aisle, stock)
        self.expir_date = expir_date

    #TODO: ADD repr
    def __str__(self):
        return f"{super().__str__()} Experation Date: {self._expir_date}"
    
    def to_dict(self):
        # ** unpacks all key value pairs from parent into a new dictionary
        return {**super().to_dict() , 'expir_date': self._expir_date}


    @property
    def expir_date(self):
        return self._expir_date
    @expir_date.setter
    def expir_date(self, new_expir_date):
        if not new_expir_date.strip():
            raise ValueError("Please enter a valid Experation date")
        self._expir_date = new_expir_date
        


    