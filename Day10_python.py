#Check if a string is a palindrome. 
print ("\nSubi - Day 10 of #100DaysOfCode\n")
print("\nCheck if a string is a palindrome\n")

def isPalindrome(string): 
    if (string == string[::-1]) : 
        return "The string is a palindrome." 
    else: 
        return "The string is not a palindrome." 
string = input ("Enter string: ") 
 
print(isPalindrome(string)) 