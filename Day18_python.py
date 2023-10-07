#Calculate the factorial of a number using a for loop
print ("\nSubi - Day 18 of #100DaysOfCode\n") 
print("\nCalculate the factorial of a number using a for loop\n")

n = int(input("Enter n:")) 
fact = 1 
for i in range(2, n+1): 
    fact *= i 
print("Factorial of {} is:{}".format(n, fact))


#Print a pattern of stars using nested loops
print("\nPrint a pattern of stars using nested loops\n")

for i in range(3):
    for j in range(i):
        print('#', end='')
    print('#')    
