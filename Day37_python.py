#Create a custom exception class and raise it in your code.
print ("\nSubi - Day 37 of #100DaysOfCode\n") 
print("\na custom exception class and raise it in your code\n")

class MyCustomException(Exception):

    def __init__(self, message):

        super().__init__(message)

def example_function(number):
    if number < 0:
        raise MyCustomException("The number must be positive.")

try:
    example_function(-3)
except MyCustomException as e:
    print(e)


#Use the finally block to ensure cleanup code is executed.
print("\nUse the finally block to ensure cleanup code is executed\n")

try:
    x = 600 / 0
except ZeroDivisionError:
    print("Divisible by zero")
finally:
    print("Final block: This will always be printed.")
