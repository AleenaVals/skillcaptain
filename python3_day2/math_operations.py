# You have been given a Python module called `math_operations.py` that contains various mathematical functions. 
#Your task is to create a Python script that imports this module and utilizes its functions to perform mathematical operations.

# Requirements:
# 1. Create the `math_operations` module and import it into your Python script. Note: Ensure that the `math_operations.py` module is in the same directory as your Python script for successful import.
# 2. In the script, use the `add` function from the `math_operations` module to add two numbers and print the result.
# 3. Use the `subtract` function from the `math_operations` module to subtract two numbers and print the result.
# 4. Use the `multiply` function from the `math_operations` module to multiply two numbers and print the result.
# 5. Use the `divide` function from the `math_operations` module to divide two numbers and print the result.
# 6. Use the `power` function from the `math_operations` module to calculate the power of a number and print the result.
# 7. Create additional mathematical operations using the available functions in the `math_operations` module and print the results.
# 8. Document your script with comments to explain the purpose of each operation.


def add(x,y):
    result_add= x+y
    print(f"The sum of {x} and {y} is {result_add}") 

def subtract(x,y):
    result_subtract= x-y
    print(f"The difference of {x} and {y} is {result_subtract}") 

def multiply(x,y):
    result_multiply= x*y
    print(f"The product of {x} and {y} is {result_multiply}") 


def divide(x,y):
    if y != 0:
        result_divide= x//y
        print(f"The quotient of {x} and {y} is {result_divide}")  
    else:        
        print("Division by zero is not possible")
    
def remainder(x,y):
    if y != 0:
        result_remainder= x%y
        print(f"The remainder of {x} and {y} is {result_remainder}")  
    else:        
        print("Division by zero is not possible")
        
    
def power(x,y):
    result_power= x**y
    print(f"{x} to the power {y} gives {result_power}") 


