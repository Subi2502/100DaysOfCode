#Implement a function to check if a string is a palindrome.
print ("\nSubi - Day 24 of #100DaysOfCode\n") 
print("\nfunction to check if a string is a palindrome\n")

def is_palindrome(s, c):
    if c == True:
        s == s.upper()
    if s == s[::-1]:
        return True
    else:
        return False
print(is_palindrome("TaT",True))    


#Create a function that accepts a list of words and returns the longest word.
print("\nfunction that accepts a list of words and returns the longest word\n")

words = input("Enter a list of words: ").split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)