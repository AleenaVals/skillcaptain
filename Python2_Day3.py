# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:00:05 2023

@author: aleen
"""

'''
Create a child class named "Truck" that inherits from the Vehicle class. 
Add an additional attribute "load_capacity" to the Truck class. 
Implement a method called "display_info()" that prints the brand, model, and load capacity of the truck. 
Override the "display_info()" method to include the load capacity in the output.

'''

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def display_info(self):
        print(f"Brand:{self.brand}, Model:{self.model}")
        
class Truck(Vehicle):
    def __init__(self, brand, model,load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity
        
    def display_info(self):
        print(f"Brand:{self.brand}, Model:{self.model}, Load Capacity:{self.load_capacity}")
        
        
truck= Truck("Ford","F150",1000)

truck.display_info()
