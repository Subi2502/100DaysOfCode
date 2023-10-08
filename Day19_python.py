#Implement a basic calculator program using a menu-driven approach 
# print ("\nSubi - Day 19 of #100DaysOfCode\n") 
# print("\nBasic calculator program using a menu-driven approach\n")

# def calc():
#     while True:
#         print("1. Addition") 
#         print("2. SUbtraction")
#         print("3. Multiplication")
#         print("4. Division")
#         print("5. Exit")
#         opt = int(input("Enter your choice:"))
#         if opt == 1:
#             n1 = int(input("Enter no1:"))
#             n2 = int(input("Enter no2:"))
#             res = n1 + n2
#             print("The result is:",res)
#         elif opt == 2:
#             n1 = int(input("Enter no1:"))
#             n2 = int(input("Enter no2:"))
#             res = n1 - n2
#             print("The result is:",res)
#         elif opt == 3:
#             n1 = int(input("Enter no1:"))
#             n2 = int(input("Enter no2:"))
#             res = n1 * n2
#             print("The result is:",res)
#         elif opt == 4:
#             n1 = int(input("Enter no1:"))
#             n2 = int(input("Enter no2:"))
#             res = n1 / n2
#             print("The result is:",res)
#         elif opt == 5:
#             print("Thank you!")
#             break
#         ch = input("Press N to Exit:")
#         if ch in 'Nn':
#             break
# calc()


#Write a program to find the GCD (Greatest Common (Greatest Common Divisor) of two numbers using a while loop.
print("\na program to find the GCD of two numbers using a while loop\n")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
i = 1
while(i<=a and i<=b):
    if(a%i==0 and b%i==0):
        gcd=i
    i = i+1
print("GCD is:", gcd)
