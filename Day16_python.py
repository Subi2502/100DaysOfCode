#Calculate the sum of all even numbers between 1 and 100 using a for loop
# print ("\nSubi - Day 16 of #100DaysOfCode\n") 
# print("\nthe sum of all even numbers between 1 and 100 using a for loop\n")

# total = 0

# for number in range(101):
#     if number % 2 == 0:
#         total = total + number
# print("The sum of the even numbers (0-100) : ", total) 


#Write a program to check if a number is prime using a while loop
print("\ncheck if a number is prime using a while loop\n")

num = int(input("Enter a number ( greater than 1)"))  
f = 0
i = 2
while i <= num / 2:
    if num % i == 0:
        f=1
        break
    i=i+1
    
if f==0:
    print("The entered number is a PRIME number")
else:
    print("The entered number is not a PRIME number")


