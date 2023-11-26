#Write a program to implement a priority queue.
print ("\nSubi - Day 68 of #100DaysOfCode\n") 
print("\nWrite a program to implement a priority queue\n")

import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    def dequeue(self):
        return heapq.heappop(self.queue)[1]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    

pq = PriorityQueue()
pq.enqueue('Task 1', 3)
pq.enqueue('Task 2', 1)
pq.enqueue('Task 3', 2)


while not pq.is_empty():
    print(pq.dequeue())