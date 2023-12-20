#Write a program to find the longest palindromic substring in a string.
print ("\nSubi - Day 92 of #100DaysOfCode\n") 
print("\nWrite a program to find the longest palindromic substring in a string\n")

def longest_palindromic_substring(s):

  longest_palindromes = [[False for _ in range(len(s))] for _ in range(len(s))]

  for length in range(len(s), 0, -1):
    for start in range(0, len(s) - length + 1):
      if s[start:start + length] == s[start:start + length][::-1]:
        longest_palindromes[start][start + length - 1] = True

  longest_palindrome = ""
  for start in range(0, len(s)):
    for end in range(start, len(s)):
      if longest_palindromes[start][end] and end - start + 1 > len(longest_palindrome):
        longest_palindrome = s[start:end + 1]

  return longest_palindrome


if __name__ == "__main__":
  s = "Pyhon programming"
  print(longest_palindromic_substring(s))  