#Implement a function to find the LCM (Least Common Multiple) of two numbers.
# print ("\nSubi - Day 23 of #100DaysOfCode\n") 
# print("\nfunction to find the LCM of two numbers\n")

# def find_lcm(x, y):
#     max = x if x > y else y
#     while True:
#         if max % x == 0 and max % y == 0:
#             return max
#         max +=1
# a = int(input("Enter First Number :"))
# b = int(input("Enter Second Number :"))
# lcm_result = find_lcm(a, b)
# print("LCM is : ", lcm_result)


#Create a function to generate a list of prime numbers up to a given limit.
print("\nfunction to generate a list of prime numbers up to a given limit\n")

start = int(input("Enter the starting range:"))
end = int(input("Enter the end range:"))
print("prime numbes in the range", start, "to", end)
for i in range(start, end+1):
    flag = 0
    for j in range(2, i):
        if(i % j == 0):
            flag = 1
            break  
        if(flag == 0):
            print(i, end = ' ')