# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:33:24 2023

@author: aleen
"""

'''
*1. Create a class called "Product" that represents a product in the e-commerce system. The class should have attributes for the product name, price, and quantity.*

*2. Create a class called "Cart" that represents the user's shopping cart. The cart should have attributes for the user's name and a list to store the added products.*

*3. Implement methods in the "Cart" class to add a product to the cart, remove a product from the cart, and display the cart's contents.*

*4. The "add_to_cart" method should take a "Product" object as a parameter and add it to the cart's list of products.*

*5. The "remove_from_cart" method should take a product name as a parameter and remove the corresponding product from the cart.*

*6. The "display_cart" method should display the products in the cart along with their details.*

'''



class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:
    def __init__(self, username):
        self.username = username
        self.products = []

    def add_to_cart(self):
        while True:
            name = input("Enter the name of the product: ")
            if not name.replace(" ", "").isalpha():
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

        product = Product(name, price, quantity)
        self.products.append(product)
        print(f"{product.name} has been added to the cart.")

    def remove_from_cart(self):
        product_name = input("Enter the name of the product to remove: ")
        removed = False
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"{product.name} has been removed from the cart.")
                removed = True
                break
        if not removed:
            print(f"{product_name} not found in the cart.")

    def display_cart(self):
        print(f"Shopping Cart for {self.username}:")
        for product in self.products:
            print(f"Product:{product.name}")
            print(f"Price: {product.price}")
            print(f"Quantity: {product.quantity}")
            print()

    def choice(self):
        while True:
            print("\nWhat would you like to do?")
            print("1. Add a product to the cart")
            print("2. Remove a product from the cart")
            print("3. Display the cart's contents")
            print("4. Exit")

            option = input("Enter your choice: ")

            if option == "1":
                self.add_to_cart()
            elif option== "2":
                self.remove_from_cart()
            elif option == "3":
                self.display_cart()
            elif option == "4":
                print("Thank you for using the cart. Exiting.")
                break
            else:
                print("Invalid choice. Please try again.")



username = input("Enter your username: ")
cart = Cart(username)

cart.choice()
