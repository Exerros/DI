import random

# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

# def display_message():
#     print("I'm taking python course")

# display_message()



# 🌟 Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

# def favorite_book(title):
#     print(f"One of my favorite books is {title}")
    
# favorite_book("Ender's Game")



#  Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

# def describe_city(city=None, country=None):
#     print(f"{city} is in {country}")

# describe_city("Reykjavik", "Iceland")

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.


### import random is on the 1st line
# def random_number(num):
#     if num <1 or num > 100:
#         print(f"{num} is not between 1 and 100, choose again")
#     else:
#         random_num = random.randint(1, 100)
#         if num == random_num:
#             print("success!!")
#         else:
#             print(f"fail {num} , {random_num}")
    
# random_number(int(input("choose a number between 1 and 100: " )))



# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments. 

# def make_shirt(size = "L", text= "I love Python"):
#     print(f"The size of the shirt is {size} and the text is {text}")

# make_shirt()
# make_shirt("M", )
# make_shirt("XL", "This is fun")
# make_shirt(text = "is this a key?", size= "s")



# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

# def show_magicians(magician_names):
#     for magician_name in magician_names:
#         print(magician_name)
    
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# show_magicians(magician_names)

# def make_great(magician_names):
#     for i in range(len(magician_names)):
#         magician_names[i] = "The Great " + magician_names[i]
#     return magician_names

# make_great(magician_names)
        
# show_magicians(magician_names)



# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

# def get_random_temp():
#     number = random.randint(-10, 40)
#     f"{number} degrees (Celsius) "
#     return number

# def main():
#     get_random_temp()
#     x = get_random_temp()
#     print(f"The temperature right now is {x}")
#     if x < 0:
#         print("{x} Brrr, that's freezing! Wear some extra layers today")
#     elif x >= 0 and x <16:
#         print (f"{x} Quite chilly! Don't forget your coat")
#     elif x >= 16 and x <=23 :
#         print (f"{x} It's nice, not too cold not too hot")
#     elif x >= 24 and x <32 :
#         print (f"{x} It's too hot, at least gor me")
#     elif x >= 32 and x <=40 :
#         print (f"{x} This is HELL")
        
def get_random_temp(season):
    if season == 'winter' :
        number = random.randint(-10, 16)
    elif season == 'autumn' :
        number = random.randint(10,20)
    elif season == 'summer' :
        number = random.randint(26,34)
    else :
        number = random.randint(16,24)
    return number



        
def main():
    season = input("enter the season: ")
    x = get_random_temp(season)
    print(f"The temperature right now is {x} degrees (Celsius)")
    if x < 0:
        print("{x} Brrr, that's freezing! Wear some extra layers today")
    elif x >= 0 and x <16:
        print (f"{x} degrees, Quite chilly! Don't forget your coat")
    elif x >= 16 and x <=23 :
        print (f"{x} degrees, It's nice, not too cold not too hot")
    elif x >= 24 and x <32 :
        print (f"{x} degrees ,It's too hot, at least gor me")
    elif x >= 32 and x <=40 :
        print (f"{x} degrees? This is HELL")
            



main()