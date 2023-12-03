#Write a program to implement a selection sort algorithm.
print ("\nSubi - Day 75 of #100DaysOfCode\n") 
print("\nWrite a program to implement a selection sort algorithm\n")

def selection_sort(array):
  
  for i in range(len(array)):
    
    min_index = i
    for j in range(i + 1, len(array)):
      if array[j] < array[min_index]:
        min_index = j

    array[i], array[min_index] = array[min_index], array[i]

  return array

array = [5, 3, 2, 1, 4]
sorted_array = selection_sort(array)
print(sorted_array)