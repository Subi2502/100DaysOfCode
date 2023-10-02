#Replace all occurrences of a character in a string
print ("\nSubi - Day 13 of #100DaysOfCode\n") 
print("\nReplace all occurrences of a character in a string\n")

string = input("Enter string:")
string = string.replace('a','$')
string = string.replace('A','$')
print("Modified string: ")
print(string)

#Reverse a string
print("\nReverse a string\n")
 
txt = "Python Coding"[::-1]
print(txt)

#Count the occurrences of a word in a text
print("\nCount the occurrences of a word in a text\n")

Test_str = "Python programming"
count = 0
for i in Test_str:
    if i == 'o':
        count = count + 1
print("Count of o in Python Programming is :" + str(count))        