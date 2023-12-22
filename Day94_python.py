#Write a program to find the top k frequent elements in a list.
print ("\nSubi - Day 94 of #100DaysOfCode\n") 
print("\nWrite a program to find the top k frequent elements in a list\n")

class Solution(object):
   def topKFrequent(self, nums, k):
      number_frequency = {}
      frequency_list ={}
      for i in nums:
         if i not in number_frequency:
            number_frequency[i] = 1
         else:
            number_frequency[i] += 1
      for key,value in number_frequency.items():
         if value not in frequency_list:
            frequency_list[value] = [key]
         else:
            frequency_list[value].append(key)
      result = []
      for i in range(len(nums),0,-1):
         if i in frequency_list:
            result.extend(frequency_list[i])
         if len(result) >=k:
            break
      return result
ob1 = Solution()
print(ob1.topKFrequent([2,2,2,5,5,8,8,8], 3))