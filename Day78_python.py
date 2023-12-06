#Write a program to implement a quick sort algorithm.
print ("\nSubi - Day 78 of #100DaysOfCode\n") 
print("\nWrite a program to implement a quick sort algorithm\n")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [8, 4, 3, 7, 7, 2, 5]
sorted_arr = quick_sort(arr)
print("Original Array:", arr)
print("Sorted Array:", sorted_arr)
