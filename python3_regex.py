# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:38:34 2023

@author: aleen
"""

import re

def check_password_strength(password):
    criteria = {'length': re.compile(r'.{10,}'),
        'lowercase letters': re.compile(r'[a-z]'),
        'uppercase letters': re.compile(r'[A-Z]'),
        'digits': re.compile(r'\d'),
        'special characters': re.compile(r'[!@#$%^&*()_+=\-~`:";,.<>?/]')}
    
    score = 0
    met_criteria = []

    for key, pattern in criteria.items():
        if re.search(pattern, password):
            score= score+1
            met_criteria.append(key)

    print(f"Your password score is: {score}/5")

    if score <= 2:
        print("The password is weak. Please ensure that it meets all the criteria.")
    elif score > 2 and score < 5:
        print("The password is medium strength. Please check if it has met all the criteria.")
    else:
        print("The password is strong.")        
        
    print()    
    if len(met_criteria) < len(criteria):
        print("The password does not meet the following conditions:")
        for key in criteria.keys():
            if key not in met_criteria:
                print(f"- {key}")

print()
print('''Ensure that your password:
    - contains at least 10 characters.
    - contains digits, uppercase, and lowercase letters.
    - contains special characters.''')
                  
password = input("Enter your password:")
print()
check_password_strength(password)
