# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 08:06:08 2023

@author: aleen
"""

'''
Create a Python program that converts a list into a set and vice versa.

Requirements:
Define a list with some elements.
Implement a function that converts the list into a set.
Implement another function that converts a set into a list.
Print the converted list and set.
'''

my_list=['a','e','i','o','u']

def list_to_set(l):
    print("The list is:",l)
    return set(l)
    
def set_to_list(s):
    print("The set is:",s)
    return list(s)


new_set=list_to_set(my_list)
print("The corresponding set is:",new_set)

print()
print()

new_list=set_to_list(new_set)
print("The corresponding list is:", new_list)


