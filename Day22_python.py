#Create a function to calculate the area of a rectangle.
# print ("\nSubi - Day 22 of #100DaysOfCode\n") 
# print("\nCreate a function to calculate the area of a rectangle\n")

# def rectangle_area(base, height): 
#     area = base*height 
#     print("The area is " + str(area)) 

# rectangle_area(12,42)


#Write a function to check if a number is a perfect square.
print("\nWrite a function to check if a number is a perfect square\n")

import math
def is_perfect_square(x):
    sqrt_value = math.sqrt(x)
    return int(sqrt_value) ** 2 == x
number = int(input("Enter a number:"))
if is_perfect_square(number):
    print("It is a perfect square.")
else:
    print("It is not a perfect")