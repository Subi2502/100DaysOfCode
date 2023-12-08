#Write a program to find the edit distance between two strings (Levenshtein distance).
print ("\nSubi - Day 80 of #100DaysOfCode\n") 
print("\nWrite a program to find the edit distance between two strings (Levenshtein distance)\n")

def distance(s1, s2):  
     m, n = len(s1), len(s2)  
     dp = [[0 for j in range(n+1)] for i in range(m+1)]  
     for i in range(m+1):  
        dp[i][0] = i  
        for j in range(n+1):  
          dp[0][j] = j  
        for i in range(1, m+1):  
         for j in range(1, n+1):  
          if s1[i-1] == s2[j-1]:  
           dp[i][j] = dp[i-1][j-1]  
          else:  
           dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)  
        return dp[m][n]  
     
s1 = "python"  
s2 = "chasing"  
print(distance(s1, s2))   
s1 = "Running"  
s2 = "dropping"  
print(distance(s1, s2))