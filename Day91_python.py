#Write a program to implement a queue using two stacks.
print ("\nSubi - Day 91 of #100DaysOfCode\n") 
print("\nWrite a program to implement a queue using two stacks\n")
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1[-1])
                self.s1.pop()

        if len(self.s2) != 0:
            return self.s2[-1]
        return -1

    def size(self):
        return len(self.s1) + len(self.s2)

    def is_empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
