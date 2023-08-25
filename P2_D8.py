# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:21:07 2023

@author: aleen
"""

'''
You are tasked with creating a product registration system using object-oriented programming (OOP) principles in Python. 
The system should allow users to register products by providing their details and storing them in a product database.

Requirements:
1. Create a class called "Product" that represents a product in the registration system.
2. The "Product" class should have attributes for the product name, price, and quantity.
3. Implement a constructor in the "Product" class that takes the name, price, and quantity as parameters and 
initializes the attributes.
4. Implement a method in the "Product" class that displays the product's information.
5. Create a product registration function that interacts with the user to collect the product details and 
creates a new "Product" object.
6. Store the registered product information in a product database (can be a list or a file).
'''

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        
    def display_info(self):
        print("Name:",self.name)
        print("Price:",self.price)
        print("Quantity:",self.quantity)
        
        
def product_registration(product_list):    
    while True:
        name = input("Enter product name: ")
        if not name.replace(" ","").isalpha():
            print("Product name must contain only alphabetic characters. Please try again.")
            continue
        break
    
    
    while True:
        price = input("Enter price: ")
        try:
            price = float(price)
            break
        except ValueError:
            print("Price must be a float. Please try again.")
            continue
    
    while True:   
        quantity = input("Enter quantity: ")
        try:
            quantity = float(quantity)
            break
        except ValueError:
            print("Quantity must be a float. Please try again.")
            continue    

    product = Product(name,price,quantity)
    product_list.append(product)
    
    print()
    print("Your product is registered!")
    

product_list=[]

while True:
    product_registration(product_list)
    
    choice = input("Do you want to register another product? (yes/no): ")
    print()
    if choice.lower() != "yes":
        break

print("List of products and their details:")

for product in product_list:
    product.display_info()
    print()
    

    
        
        