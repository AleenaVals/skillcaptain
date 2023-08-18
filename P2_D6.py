# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:46:21 2023

@author: aleen
"""

'''

Imagine you are a creative writer who loves to come up with interesting and unique character names. 
Your task is to create a Python program that generates a list of character names and saves them in a file.

*Requirements:*

*The program should ask the user for the number of character names to generate.*

*Each character name should consist of a random combination of three syllables.*

*The program should generate unique character names and ensure that no two names are the same.*

*Save the generated character names in a text file named "character_names.txt", with each name on a new line.*

'''

import random

def generate_name():
    syllables = ['ab', 'ac', 'ad', 'ba', 'be', 'bi', 'da', 'de', 'di', 'la', 'le', 'li', 'ma', 'me', 'mi', 'na', 'ne', 'ni', 'pa', 'pe', 'pi', 'ra', 're', 'ri', 'sa', 'se', 'si', 'ta', 'te', 'ti']
    random_syllables = random.sample(syllables, 3)
    character_name = ''.join(random_syllables)
    return character_name

num_chars = int(input("Enter the number of character names to generate: "))

character_set = set() #since sets do not allow duplicates

while len(character_set) < num_chars: 
    names = generate_name()
    character_set.add(names)


with open("character_names.txt", "w") as file:
    for name in character_set:
        file.write(name + "\n")

print("Done")
