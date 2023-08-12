# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:11:43 2023

@author: aleen
"""

'''Write a program using a while loop to print all the numbers from 1 to 10.
Create a list of names. Use a for loop to iterate over the list and print a personalized greeting for each name.'''

num =1
while num<=10:
    print(num)
    num=num+1

print()
print()    

names=['Akanksha','Harsh']
for name in names:
    print(f"Hi {name}! Thanks for building SkillCaptain. I am loving it!")
