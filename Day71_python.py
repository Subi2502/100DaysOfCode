#Write a program to implement a breadth-first search (BFS) algorithm.
print ("\nSubi - Day 71 of #100DaysOfCode\n") 
print("\nWrite a program to implement a breadth-first search (BFS) algorithm\n")

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()

            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)

                if vertex in self.graph:
                    queue.extend(self.graph[vertex])

if __name__ == "__main__":
    
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(3, 7)

    print("BFS starting from node 1:")
    g.bfs(1)
