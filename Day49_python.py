#Write a program to find the longest common prefix of a list of strings.
print ("\nSubi - Day 49 of #100DaysOfCode\n") 
print("\nprogram to find the longest common prefix of a list of strings\n")

strs = ["Cat", "Cube", "Catch"]

def longestCommonPrefix(strs):
    l = len(strs[0])
    for i in range(1, len(strs)):
        length = min(l, len(strs[i]))
        while length > 0 and strs[0][0:length] != strs[i][0:length]:
            length = length - 1
            if length == 0:
                return 0
    return strs[0][0:length]

print(longestCommonPrefix(strs))