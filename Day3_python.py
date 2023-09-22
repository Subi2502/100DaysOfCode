#Check if a number is even or odd. 
print ("\nSubi - Day 3 of #100DaysOfCode\n")
print("\nif a number is even or odd program \n")

a = int(input("the number is even or odd:"))
if(a % 2) == 0:
    print("the number is even")
else:
    print("the number is odd")

#Generate a list of even numbers between 1 and 50.
print("\nlist of even numbers between 1 and 50 program\n")
 
for num in range(1,50):
    if num%2==0:
        print (num)

#Find the factorial of a number. 
print("\nfactorial of a number problem\n")

number = int(input("Enter the number:"))
factorial = 1
if(number < 0):
    print("can't compute factorial for negative number")
elif(number < 2):
    print("{}! = {}".format(number, factorial))
else:
    for num in range(number, 1, -1):
        factorial = factorial * num
    print("{}! = {}".format(number, factorial))

