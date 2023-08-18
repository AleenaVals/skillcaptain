# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:30:57 2023

@author: aleen
"""

'''
Write a Python program that reads a text file called "data.txt" and counts the number of lines in the file.
'''


file_path = 'data.txt'

try:
    with open(file_path,'r') as file:
        lines = file.readlines() #read the number of lines in the file
        length = len(lines) 
        print(f"Number of lines in the file is {length}")
        
except FileNotFoundError:
    print(f"{file_path} not found")    
    
    
        
