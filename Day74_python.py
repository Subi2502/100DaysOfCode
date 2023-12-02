#Write a program to reverse words in a sentence.
print ("\nSubi - Day 74 of #100DaysOfCode\n") 
print("\nWrite a program to reverse words in a sentence\n")

def reverse_words(text):
  words = text.split()
  words = words[::-1]
  return ' '.join(words)

print(reverse_words('Python Programming'))


#Write a program to implement a bubble sort algorithm.
print("\nWrite a program to implement a bubble sort algorithm\n")

def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

arr = [2,4,6,8,97,43,56,34,5]
print("Before sorting:", arr)
arr = bubble_sort(arr)
print("After sorting:", arr)