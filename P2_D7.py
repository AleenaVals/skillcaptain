# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:45:58 2023

@author: aleen
"""

'''
You are tasked with creating a user registration system for an e-commerce website using object-oriented programming (OOP) principles in Python. 
The system should allow users to create an account with their personal information and store it in a user database.

Requirements:
1. Create a class called "User" that represents a user in the e-commerce system.
2. The "User" class should have attributes for the user's name, email, and password.
3. Implement a constructor in the "User" class that takes the name, email, and password as parameters and initializes the attributes.
4. Implement a method in the "User" class that displays the user's information.
5. Create a user registration function that interacts with the user to collect their information and creates a new "User" object.
6. The user registration function should validate the email address and ensure that it is unique among registered users.
7. Store the registered user information in a user database (can be a list or a file).

'''

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Password: {'*' * len(self.password)}")


def is_email_unique(email, user_list):
    for user in user_list:
        if user.email == email:
            return False
    return True


def user_registration(user_list):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    if not is_email_unique(email,user_list):
        print("Email already exists!")
        return
    
    user = User(name, email, password)
    user_list.append(user)
    
    print()    
    print("User registration successful!")


user_list = []


while True:
    user_registration(user_list)

    choice = input("Do you want to register another user? (yes/no): ")
    if choice.lower() != "yes":
        break

print()
print("Registered Users:")
print()

for user in user_list:
    user.display_info()
    print()
