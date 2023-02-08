# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.


number:int=int(input("choose number: "))
length:int=int(input("choose length: "))
result=[]

for i in range(1,length+1):
    mult= number * i
    result.append(mult)

print(result)
    
    

# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"


# word= list(input("Enter a string: "))


word:str=str(input("Enter a word with dublicate letters: "))

result=""

for i in range(len(word)):
    if i == 0:
        result += word[i]
    elif word[i] != word[i-1]:
       result += word[i]
       
print (result)
