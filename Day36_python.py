#Write a program that handles exceptions for division by zero.
print ("\nSubi - Day 36 of #100DaysOfCode\n") 
print("\na program that handles exceptions for division by zero\n")

def zero_exception(x, y):
    try:
        return(x / y)
    except ZeroDivisionError:
        print("Error: dividing by zero")
        return None
    
print(zero_exception(15, 8))
print(zero_exception(15, 0))


#Implement a try-except block to catch a specific exception.
print("\nImplement a try-except block to catch a specific exception\n")

try:
    file = open("myfile.txt")
    contents = file.read()
    file.close()
except FileNotFoundError:
    print("Error: File does not exist.")