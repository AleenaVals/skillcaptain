# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:53:10 2023

@author: aleen
"""

'''Write a program that takes two numbers from the user and performs the following operations:

Requirements:

1. Add the two numbers and print the result.

2. Subtract the second number from the first number and print the result.

3. Multiply the two numbers and print the result.

4. Divide the first number by the second number and print the result.'''



a =int(input("Enter first number:"))

b= int(input("Enter second number:"))

s=a+b
print(f"Sum of {a} and {b} is {s}")

d=a-b
print(f"Difference of {a} and {b} is {d}")

p =a*b
print(f"Product of {a} and {b} is {p}")

q = a/b
print(f"Quotient of {a} and {b} is {q}")