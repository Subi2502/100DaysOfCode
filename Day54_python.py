#Write a program to find the factorial of a number using a for loop.
print ("\nSubi - Day 54 of #100DaysOfCode\n") 
print("\nprogram to find the factorial of a number using a for loop\n")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    
    fact = factorial(num)
    print(f"The factorial of {num} is: {fact}")


#Write a program to implement a priority queue.
print("\nprogram to implement a priority queue\n")

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

pq = PriorityQueue()
pq.push('Task 1', 3)
pq.push('Task 2', 1)
pq.push('Task 3', 2)

print(pq.pop()) 
print(pq.pop())  
print(pq.pop())  
