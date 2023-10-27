#Create a generator function that generates Fibonacci numbers.
print ("\nSubi - Day 41 of #100DaysOfCode\n") 
print("\nCreate a generator function that generates Fibonacci numbers\n")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(5):

    print(next(fib))


#Use regular expressions to validate email addresses.
print ("\nRegular expressions to validate email addresses\n") 

import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email")


isValid("subiii.subi@gmail.com")
isValid("subi123@yahoo.co.uk")
isValid("subii123@...uk")
isValid("...@domain.us")
