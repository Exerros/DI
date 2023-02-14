# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

# def exercise1():
#     ''' this is the first exercise '''
#     print(abs(-5))

#     print(int("7"))

#     hello= input("type hi: ")
#     print(hello)

# print(exercise1.__doc__)



class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        
    def __str__(self):
        if self.amount > 1:
            return f"{self.amount} {self.currency}s"
        else:
            return f"{self.amount} {self.currency}"
        
    def __int__(self):
        return self.amount
    
    def __repr__(self) -> str:
        return str(self) 
    
    def __add__(self, amount_to_add_or_maybe_currency_object):
        if isinstance(amount_to_add_or_maybe_currency_object, Currency):
            
             otherCurrency: Currency = amount_to_add_or_maybe_currency_object
             
             if self.currency != otherCurrency.currency:
                 error = f"Cannot add between Currency type {self.currency} and {otherCurrency.currency}"
                 raise TypeError(error)            

        return self.amount + int(amount_to_add_or_maybe_currency_object)
    
    def __iadd__(self, amount_to_add_or_maybe_currency_object):
        
        self.amount = self + amount_to_add_or_maybe_currency_object
        return self
        
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1)
# 5 dollars

c1 += 5
print(c1)
# c1
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>