# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:30:57 2023

@author: aleen
"""

'''
Write a Python program that reads a text file called "data.txt" and counts the number of lines in the file.
'''


try:
    with open(r'C:\Users\aleen\Desktop\data.txt','r') as file:
        lines = file.readlines()
        length = len(lines)
        print(f"Number of lines in the file is {length}")
except FileNotFoundError:
    print("File not found")
    
    
        