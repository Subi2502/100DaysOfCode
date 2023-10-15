#Implement a recursive function to calculate the Fibonacci sequence
print ("\nSubi - Day 26 of #100DaysOfCode\n") 
print("\na recursive function to calculate the Fibonacci sequence\n")

def fibonacci(n):

    if n == 1:
        return 0
    
    if n == 2:
        return 1
    
    return fibonacci(n-1)+fibonacci(n-2)

for i in range(1,10):
    print(fibonacci(i))


#Create a dictionary to store the names and ages of people
print("\na dictionary to store the names and ages of people\n")

person = {"name": "subi", "age": "20"}

print(person)

#Write a program to find the common elements between two lists
print("\na program to find the common elements between two lists\n")

def common_element(a,b):
    a_set = set(a)
    b_set = set(b)

    if(a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
common_element(a,b)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
common_element(a,b)