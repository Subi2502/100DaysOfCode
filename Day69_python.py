#Write a program to find the kth smallest element in an unsorted list.
print ("\nSubi - Day 69 of #100DaysOfCode\n") 
print("\nWrite a program to find the kth smallest element in an unsorted list\n")

import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return quickselect(arr, low, pivot_index - 1, k)

def kth_smallest(arr, k):
    if k > 0 and k <= len(arr):
        return quickselect(arr, 0, len(arr) - 1, k - 1)
    else:
        return None

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k_value = 3
result = kth_smallest(my_list, k_value)

if result is not None:
    print(f"The {k_value}th smallest element is: {result}")
else:
    print(f"Invalid value of k")
