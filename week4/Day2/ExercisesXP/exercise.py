# 🌟 Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers= {5,25,45,125}
new_numbers = {2,4,6}
my_fav_numbers.update(new_numbers)
my_fav_numbers.pop()
print(my_fav_numbers)
