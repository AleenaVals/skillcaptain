# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 08:24:12 2023

@author: aleen
"""

'''
Write a program that takes two numbers as input from the user and performs division. 
Handle the potential division by zero error.

'''

while True:
    try:
        num1= int(input("Enter first number:"))
        break
    except ValueError:
        print("Please enter an integer value")
        
    
while True:
    try:
        num2= int(input("Enter second number:"))
        if num2==0:
            print("Divison by zero is not possible")
        else:
            break
    except ValueError:
        print("Please enter an integer value")




q=num1/num2
print()
print(f"The quotient is {q}")
