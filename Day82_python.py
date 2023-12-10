#Write a program to check if a list is a palindrome.
print ("\nSubi - Day 82 of #100DaysOfCode\n") 
print("\nWrite a program to check if a list is a palindrome\n")

def palindrome(list1):

  reversed_list = list1[::-1]

  if list1 == reversed_list:
    return True
  else:
    return False

list1 = [1, 2, 3, 2, 1]
print(palindrome(list1))  


#Write a program to find the intersection of two sets.
print("\nWrite a program to find the intersection of two sets\n")

def intersection(set1, set2):

    intersection_method_result = set1.intersection(set2)
    
    intersection_operator_result = set1 & set2
    
    return intersection_method_result, intersection_operator_result

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

result_method, result_operator = intersection(set_a, set_b)

print("Intersection using method:", result_method)
print("Intersection using operator:", result_operator)
