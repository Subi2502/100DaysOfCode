#Write a program to implement a heap data structure (min-heap or max-heap).
print ("\nSubi - Day 93 of #100DaysOfCode\n") 
print("\nWrite a program to implement a heap data structure (min-heap or max-heap)\n")

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up()

    def heapify_up(self):
        i = len(self.heap) - 1
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def pop(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down()
        return root

    def heapify_down(self):
        i = 0
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def print_heap(self):
        print(self.heap)


heap = MinHeap()
heap.insert(5)
heap.insert(10)
heap.insert(20)
heap.insert(15)
heap.insert(25)

heap.print_heap()
