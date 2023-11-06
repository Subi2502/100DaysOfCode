#Write a program to implement a simple queue.
print ("\nSubi - Day 48 of #100DaysOfCode\n") 
print("\nProgram to implement a simple queue\n")

class Queue:
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def size(self):
        return len(self.items)


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

print(queue.is_empty())

print(queue.size())