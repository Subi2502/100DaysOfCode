#Write a program to count the frequency of elements in a list using a dictionary
print ("\nSubi - Day 28 of #100DaysOfCode\n") 
print("\nprogram to count the frequency of elements in a list using a dictionary\n")

def CountFreq(list):
  freq = {}
  for items in list:
    freq[items] = list.count(items)
  print(freq)

list =['a', 's', 'a', 's', 'c', 'c', 'c','b']
CountFreq(list)


#Implement a binary search algorithm to find an element in a sorted list.
print("\na binary search algorithm to find an element in a sorted list\n")

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1