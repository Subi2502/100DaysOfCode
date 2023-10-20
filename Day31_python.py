# #Write a program to count the number of words in a text file.
# print ("\nSubi - Day 31 of #100DaysOfCode\n") 
# print("\na program to count the number of words in a text file\n")

# file = open("data.file", "rt")
# data = file.read()
# words = data.split()

# print("number of words in text file :", len(words))


# #Write a program to copy the contents of one text file to another.
# print("\na program to copy the contents of one text file to another\n")

# with open("first.txt","r") as firstfile, open("second.txt","a") as secondfile:
    
#     for line in firstfile:

#         secondfile.write(line)


import pandas as pd

nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]

dict = {'name': nme, 'degree': deg, 'score': scr}

df = pd.DataFrame(dict)
 
print(df)