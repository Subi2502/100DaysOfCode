# Convert a temperature from Celcius to Fahrenheit 
# Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32
print ("\nSubi - Day 2 of #100DaysOfCode\n")

print("\n Celcius to Farenheit program\n")
celcius = int(input("enter the celcius input:"))
fahrenheit = (celcius*9/5) + 32
print("Fahrenheit of " + str(celcius) + " celcius: ", fahrenheit)


# Create a simple calculator program with functions for addition, subtraction, multiplication, and division. 
print("\nCalculator program using python\n")

def add(x,y):
    return x+y
print(add(2,3))

def sub(x,y):
    return x-y
print(sub(2,3))

def mul(x,y):
    return x*y
print(mul(2,3))

def div(x,y):
    return x/y
print(div(2,3))
