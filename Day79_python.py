#Write a program to find the longest increasing subsequence in a list.
print ("\nSubi - Day 79 of #100DaysOfCode\n") 
print("\nWrite a program to find the longest increasing subsequence in a list\n")

def longest_increasing_subsequence(arr):
 
  n = len(arr)
  lis = [1] * n
  prev = [-1] * n

  for i in range(1, n):
    for j in range(i):
      if arr[i] > arr[j] and lis[i] < lis[j] + 1:
        lis[i] = lis[j] + 1
        prev[i] = j

  max_lis = max(lis)
  index = lis.index(max_lis)

  lis = []
  while index != -1:
    lis.append(arr[index])
    index = prev[index]

  lis.reverse()
  return lis

if __name__ == "__main__":
  arr = [45, 34, 36, 32, 97, 77, 54]
  print(longest_increasing_subsequence(arr))