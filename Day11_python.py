#Count the number of vowels in a string.  
print ("\nSubi - Day 11 of #100DaysOfCode\n")
print("\nthe number of vowels in a string\n")

string = "Python Programming"
vowels = "aeiouAEIOU"
 
count = sum(string.count(vowel) for vowel in vowels)
print(count)