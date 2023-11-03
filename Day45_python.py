#Write a program to find the intersection of two sets.
print ("\nSubi - Day 45 of #100DaysOfCode\n") 
print("\nprogram to find the intersection of two sets\n")

A = {"apple", "mango", "banana", "grape"}
B = {"apple", "banana", "grape"}
C = {"apple", "mango", "orange", "pineapple", "guava"}


print(C.intersection(B))
print(A.intersection(C))
print(B.intersection(A))


print(A.intersection(B, C))