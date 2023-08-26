# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 10:53:46 2023

@author: aleen
"""

import unittest
from cart import validation, add_product, Cart, Product

# Helper function to simulate user input
class MockInput:
    def __init__(self, values):
        self.values = values

    def input(self, prompt):
        return self.values.pop(0)

class TestValidation(unittest.TestCase):
    def test_validation(self):
        mock_input = MockInput(["Product", "12.34", "56.78"])
        with unittest.mock.patch('builtins.input', mock_input.input):
            name, price, quantity = validation()

        self.assertEqual(name, "Product")
        self.assertEqual(price, 12.34)
        self.assertEqual(quantity, 56.78)

class TestCartMethods(unittest.TestCase):
    def setUp(self):
        self.product_list = []

    def test_add_to_cart(self):
        mock_input = MockInput(["Product", "12.34", "56.78"])
        cart = Cart("TestUser")
        with unittest.mock.patch('builtins.input', mock_input.input):
            cart.add_to_cart()
        
        self.assertEqual(len(cart.products), 1)
        self.assertEqual(cart.products[0].name, "Product")
        self.assertEqual(cart.products[0].price, 12.34)
        self.assertEqual(cart.products[0].quantity, 56.78)

    def test_remove_from_cart(self):
        cart = Cart("TestUser")
        cart.products.append(Product("Product", 12.34, 56.78))

        mock_input = MockInput(["Product"])
        with unittest.mock.patch('builtins.input', mock_input.input):
            cart.remove_from_cart()

        self.assertEqual(len(cart.products), 0)

    def test_display_cart(self):
        cart = Cart("TestUser")
        cart.products.append(Product("Product", 12.34, 56.78))

        with unittest.mock.patch('builtins.print') as mock_print:
            cart.display_cart()
        
        mock_print.assert_called_with(
            "Shopping Cart for TestUser:\n"
            "Product:Product\n"
            "Price: 12.34\n"
            "Quantity: 56.78\n"
        )

if __name__ == '__main__':
    unittest.main()
