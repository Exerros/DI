# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

# Then, print the first and last characters of the given text.

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World


# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

# Hlrolelwod


sentence: str= input("Hi, please write a sentence with exactly 10 characters:")
if len(sentence) <10:
    print("The sentence is too short")
    
elif len(sentence) > 10:
    print("The sentence is too long")

print(sentence[0] +" "+ sentence[len(sentence)-1]) #  i added " " just so it will be easier to read

for x in range(len(sentence)):
    print(sentence[:x+1])


import random

suffle= "".join(random.sample(sentence,len(sentence)))
print(suffle)

    