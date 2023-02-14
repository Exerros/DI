# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

import random

def exercisetwo(number):
    num = random.randint(0, 100)
    if number == num :
        print("success")
    

# exercisetwo(3)  