#Write a program to count the frequency of elements in a list using a dictionary
# print ("\nSubi - Day 28 of #100DaysOfCode\n") 
# print("\nprogram to count the frequency of elements in a list using a dictionary\n")

# def CountFreq(list):
#   freq = {}
#   for items in list:
#     freq[items] = list.count(items)
#   print(freq)

# list =['a', 's', 'a', 's', 'c', 'c', 'c','b']
# CountFreq(list)


#Implement a binary search algorithm to find an element in a sorted list.
print("\na binary search algorithm to find an element in a sorted list\n")

def binarySearch(array, target):
    left, right = 0, len(array)-1
    while left <= right:
        middle = (left+right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1