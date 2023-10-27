#Write a program to find the intersection of two sets.
print ("\nSubi - Day 30 of #100DaysOfCode\n") 
print("\na program to find the intersection of two sets\n")

set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {4, 6, 8}

print("set1 intersection set2 : ",
      set1.intersection(set2))

print("set1 intersection set2 intersection set3 :",
       set1.intersection(set2, set3))


#Read a text file and print its content to the console.
print("\nRead a text file and print its content to the console.\n")

file = open("file.txt", "r")
contents = file.read()
print(contents)
file.close()