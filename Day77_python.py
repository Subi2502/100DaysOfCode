#Write a program to implement a merge sort algorithm.
print ("\nSubi - Day 77 of #100DaysOfCode\n") 
print("\nWrite a program to implement a merge sort algorithm\n")

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

arr = [10, 7, 8, 9, 1, 5]
print("Unsorted Array:")
print(arr)
print("\nSorted Array:")
print(merge_sort(arr))