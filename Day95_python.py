#Write a program to perform graph traversal (DFS and BFS) on a graph.
print ("\nSubi - Day 95 of #100DaysOfCode\n") 
print("\nWrite a program to perform graph traversal (DFS and BFS) on a graph\n")

class Graph:

  def __init__(self):
    self.graph = {}

  def add_edge(self, u, v):
    if u not in self.graph:
      self.graph[u] = []
    self.graph[u].append(v)

  def dfs(self, start):
    visited = set()
    stack = [start]
    while stack:
      vertex = stack.pop()
      if vertex not in visited:
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbour in self.graph[vertex]:
          stack.append(neighbour)

  def bfs(self, start):
    visited = set()
    queue = [start]
    while queue:
      vertex = queue.pop(0)
      if vertex not in visited:
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbour in self.graph[vertex]:
          queue.append(neighbour)

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("\nDFS traversal:")
graph.dfs(2)

print("\nBFS traversal:")
graph.bfs(2)


