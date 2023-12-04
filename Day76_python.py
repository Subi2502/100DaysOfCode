#Write a program to implement an insertion sort algorithm.
print ("\nSubi - Day 76 of #100DaysOfCode\n") 
print("\nWrite a program to implement an insertion sort algorithm\n")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_item
    return arr


arr = [76, 75, 53, 36, 94]
print("Unsorted Array:", arr)
print("Sorted Array:", insertion_sort(arr))