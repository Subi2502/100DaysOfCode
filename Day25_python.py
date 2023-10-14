#Write a function to find the median of a list of numbers
# print ("\nSubi - Day 25 of #100DaysOfCode\n") 
# print("\nfind the median of a list of numbers\n")

# numbers = [2, 4, 6, 8, 1, 3, 5, 7, 9]
# numbers.sort()
# length = len(numbers)
# middle = length // 2
# if length % 2 == 0:
#     median = (numbers[middle - 1] + numbers[middle]) / 2
# else:
#     median = numbers[middle]
# print("Median is :", median)


#Calculate the power of a number using a recursive function
print("\nCalculate the power of a number using a recursive function\n")

def power(x,y):
    if y == 0:
        return 1
    else:
        return x*power(x,y-1)
    
print(power(3,6))