# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }
# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }
# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

word:str= str(input("Enter a word: "))

letter_dict:dict= {}

for i, letter in enumerate(word):
    if letter not in letter_dict:
        letter_dict[letter]= [i]
    else:
        letter_dict[letter].append(i)

print(letter_dict)  




# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.

wallet:int = int(input("Enter the amount of money in your wallet: $"))

# List of items in the store and their prices
store = {"Apple": 0.99, "Banana": 0.49, "Carrot": 0.69, "Donut": 1.29, "Eggs": 2.99}

# Create a list of items that can be bought with the money in the wallet
affordable_items = []
for item, price in store.items():
    if price <= wallet:
        affordable_items.append(item)

# Sort the list of affordable items in alphabetical order
affordable_items.sort()

# Display the result
if affordable_items:
    print("You can afford:")
    for item in affordable_items:
        print(item)
else:
    print("Nothing")