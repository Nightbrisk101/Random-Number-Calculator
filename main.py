"""
Libraries I used here, my goal of this is to practice Try and Except
I am not the best at it so this is my reason.
"""

import os
import random
import time
import sys

# Defining Variables Go Here
user_number = 0
random_number = random.randint(1,100)
bool_value = "f"

# Print what random number will be added
print(f"The current random number that will be added is {random_number}")
time.sleep(2)
os.system("clear")

# Try and Except statement saying what operation it will be
while bool_value == "f":
    operation = input("Input an operation ( + - * / ): ")
        
    if operation == "+":
        bool_value = "r"
    elif operation == "-":
        bool_value ="r"
    elif operation == "*":
        bool_value = "r"
    elif operation == "/":
        bool_value = "r"

    else:
        os.system("clear")
        print("Value must be an operator!  Input an operation.")
        time.sleep(2)
        os.system("clear")
        bool_value = "f"

#Try and Except statement saying what number will be added
while bool_value == "r":
    try:
        user_number = int(input("Input an integer: "))
        
    except ValueError:
        os.system("clear")
        print("Value inputted is not a integer!  Input only integers.")
        time.sleep(2)
        os.system("clear")
        bool_value = "r"
        user_continue = input("Continue? (Y/N): ").lower()

        if user_continue == "N":
            sys.exit()
            os.system("clear")
        elif user_continue == "Y":
            os.system("clear")
            continue
        else:
            print("WIP")
     
    pass
    bool_value = "end"

#Functions
if operation == "+":
    total_number = random_number + user_number
    print(f"The sum of {random_number} and {user_number} is {total_number}")
elif operation == "-":
    total_number = random_number - user_number
    print(f"The total of {random_number} and {user_number} is {total_number}")
elif operation == "*":
    total_number = random_number * user_number
    print(f"The total of {random_number} and {user_number} is {total_number}")
elif operation == "/":
    total_number = random_number / user_number
    print(f"The quotient of {random_number} and {user_number} is {total_number}")
else:
    print("There was an error in the process!  Try again.")