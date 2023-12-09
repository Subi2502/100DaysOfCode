#Write a program to find the maximum sum subarray in a list (Kadane's algorithm).
print ("\nSubi - Day 81 of #100DaysOfCode\n") 
print("\nWrite a program to find the maximum sum subarray in a list (Kadane's algorithm)\n")

def maxSubArraySum(arr,size):
    
    max_till_now = arr[0]
    max_ending = 0
    
    for i in range(0, size):
        max_ending = max_ending + arr[i]
        if max_ending < 0:
            max_ending = 0
        
        
        elif (max_till_now < max_ending):
            max_till_now = max_ending
            
    return max_till_now

arr = [1, -2, 3, -4, 5, -6, 7]
print("Maximum Sub Array Sum Is" , maxSubArraySum(arr,len(arr)))
