# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 11:58:51 2023

@author: aleen
"""

'''
Create a class called BankAccount with the following attributes: account number, account holder name, and account balance.

*Create a constructor for the BankAccount class that initializes the account number, account holder name, and account balance.*
*Create methods to deposit and withdraw money from the account. The methods should update the account balance accordingly.*
*Create a method to display the account information, including the account number, account holder name, and account balance.*

'''

class BankAccount:
    def __init__(self,number,name,balance):
        self.acc_num = number
        self.acc_name = name
        self.acc_balance= balance
    
    def deposit(self,amount):
        print(f"The current account balance: Rs.{self.acc_balance}")
        print(f"Amount deposited: Rs. {amount}")
        self.acc_balance= self.acc_balance+amount
        print(f"The new account balance is: Rs.{self.acc_balance}")

    def withdraw(self,amount):
        print(f"The current account balance: Rs.{self.acc_balance}")
        print(f"Amount withdrawn: Rs. {amount}")
        self.acc_balance=self.acc_balance-amount
        print(f"The account balance is: Rs.{self.acc_balance}")

    def display(self):
        print(f"Account Number: {self.acc_num}")
        print(f"Account Holder Name : {self.acc_name}")
        print(f"Account Balance: Rs.{self.acc_balance}")
        
account = BankAccount("A5167","Arpita",1000)

print()

account.deposit(500)
print()
account.withdraw(200)
print()
account.display()
