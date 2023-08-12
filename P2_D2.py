# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 11:27:53 2023

@author: aleen
"""

'''
*Create a class called Person that represents a person, with properties for their name and age. 
The Person class should of a constructor that takes two parameters: a String for the person's name 
and an int for their age. The constructor should set the initial values of the name and age properties 
based on the passed-in values.*

*Once you have created the Person class and its constructor, create two Person objects: 
one representing a person named "Alice" who is 25 years old, 
and another representing a person named "Bob" who is 30 years old. 
Print out the name and age properties of each Person object.*

'''


class Person:
    def __init__(self,name:str,age:int):
            self.name=name
            self.age=age
        
        
        
alice= Person("Alice",25)
print("Name:", alice.name)
print("Age:",alice.age)

print()

bob= Person("Bob",30)
print("Name:", bob.name)
print("Age:",bob.age) 
