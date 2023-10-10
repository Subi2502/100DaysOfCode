#Print the multiplication table of a number using nested loops.
# print ("\nSubi - Day 21 of #100DaysOfCode\n") 
# print("\nPrint the multiplication table of a number using nested loops.\n")

# nums = [3, 5]
# max = 999
# result = 0
# for num in nums:
#     for i in range(1,max):
#         if num*i < max:
#             result += num*i
# print (result)
# result = 0
# for i in range(0,max):
#     if i%3 == 0 or i%5 == 0:
#         result += i
# print (result)


#Write a program to reverse a number using a while loop.
print("\nprogram to reverse a number using a while loop\n")

number = int(input("Enter the integer number: ")) 
reversed_num = 0

while number != 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number //= 10

print("Reversed Number: " + str(reversed_num))