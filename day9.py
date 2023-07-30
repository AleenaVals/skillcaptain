# -- coding: utf-8 --
"""
Created on Sun Jul 30 16:38:28 2023

@author: aleen
"""

'''
Create a Python program that performs the following operations on a given dictionary:

Add a new key-value pair to the dictionary.

Remove a specific key-value pair from the dictionary.

Update the value of a specific key in the dictionary.

Check if a key exists in the dictionary.

Print all the keys in the dictionary.

'''


my_dict={"Name":"June", "Age":25, "City":"Bengaluru"}

#adding a new key-value pair
my_dict["Occupation"]= "Data Analyst" 

#deleting a pair
del my_dict["Age"]

#updating the value
my_dict["Occupation"] ="Data Scientist" 

#checking if a key exists
if "Age" in my_dict:
    print("The key exists in the dictionary")
else:
    print("The key does not exist") 
    
# printing the keys
print(my_dict.keys()) 







