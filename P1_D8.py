# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 09:24:08 2023

@author: aleen
"""

'''
Create a Python program that concatenates two lists into a single list.

Requirements:

1. Define two separate lists.

2. Implement a function that takes both lists as input and returns a new list that 
contains the elements from both lists combined.

3. Print the concatenated list.
'''



list1 = [45,11,0.9]
list2 = ["a","b", True]

def concatenate(l1,l2):
    concatenated_list=l1+l2
    return concatenated_list

result=concatenate(list1,list2)
print("Concatenated list", result)
