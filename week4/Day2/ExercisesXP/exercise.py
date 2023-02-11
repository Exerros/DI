# 🌟 Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers= {5,25,45,125}
my_fav_numbers.add(2)
my_fav_numbers.add(4)
my_fav_numbers.remove(4)
friend_fav_numbers = {10, 20, 30, 40, 50}
our_fav_numbers= my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)



# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# answer- No, Tuple are immutable



# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("kiwi")
basket.insert(0,"Apples")
basket_len=len(basket)
print(basket_len)
basket.clear()
print(basket)



# # Exercise 4: Floats
# # Instructions
# # Recap – What is a float? What is the difference between an integer and a float?

# #answer- Float is a number that have a fractiinal component like: 10.5 or -1.0, integer is a whole number like: 0 or -25

# # Can you think of another way to generate a sequence of floats? - I don't understand the question
# # Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

result = [1.5 + i*0.5 for i in range(8)]
print(result)



# # 🌟 Exercise 5: For Loop
# # Instructions
# # Use a for loop to print all numbers from 1 to 20, inclusive.
# # Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for i in range(0,21):
    print (i)
    
    
 
# #   🌟 Exercise 6 : While Loop
# # Instructions
# # Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.  

name=""
while name != "Daniel":
    name= input("enter your name: ")
print("We got the same name")



# # Exercise 7: Favorite Fruits
# # Instructions
# # Ask the user to input their favorite fruit(s) (one or several fruits).
# # Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# # Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# # Now that we have a list of fruits, ask the user to input a name of any fruit.
# # If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# # If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fruits= input("Enter your favorite fruits, separated them by a single space: ")
fruit_list= fruits.split(" ")
# print (fruit_list)  #just to check
any_fruit=input("Enter any fruit: ")
if any_fruit in fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")



# # Exercise 8: Who Ordered A Pizza ?
# # Instructions
# # Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# # As they enter each topping, print a message saying you’ll add that topping to their pizza.
# # Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

toppings=[]
price:int= 10

while True:
    topping= input("Enter your pizza topping or print 'quit' to stop: ")
    if topping== 'quit':
        break
    toppings.append(topping)
    price+= 2.5
    print(f"{topping} is added to the list")

print(f" your toppings are : {toppings}")
print(f" your total price is {price}")


# Exercise 9: Cinemax
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

total_cost= 0
family=[]

while True:
    name = input("Enter a name (or 'done' to finish): ")
    if name == 'done':
        break
    age = int(input("Enter the age of " + name + ": "))
    family.append((name, age))
    # print(family) - just to check
    if age < 3:
        cost = 0
    elif age >= 3 and age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost 
print(f"Your total cost is {total_cost}$")


teens = ['Morty', 'Rick', 'Goku', 'Vegita']
allowed_to_enter=[]

for name in teens:
    age= int(input(f"{name} enter your age: "))
    if age >= 16 and age <= 21 :
        allowed_to_enter.append(name)
    else:
        print(f"{name} is not allowed to enter the movie")
teens=allowed_to_enter
print(f"{teens} are allowed to enter")



# Exercise 10 : Sandwich Orders
# Instructions
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches=[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made an {current_sandwich}")
    finished_sandwiches.append(current_sandwich)
print(f"Everything is ready, here is all your sandwiches {finished_sandwiches}")

# Exercise 11 : Sandwich Orders#2
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich"]
finished_sandwiches = []

print("The deli has run out of pastrami.")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches=sandwich_orders
print(finished_sandwiches) # just to check




