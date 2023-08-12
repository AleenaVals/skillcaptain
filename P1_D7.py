# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 09:18:34 2023

@author: aleen
"""

'''Define a function called is_even that takes an integer as input and 
returns True if the number is even, and False otherwise.
'''


def is_even(num):
    if num%2==0:
        return True
    else:
        return False
    
    
while True:
    try:
        number=int(input("Enter a number:"))
        break
    except ValueError:
        print("Invalid input. Please enter an integer value")
    
    
result= is_even(number)
print(result)
    
