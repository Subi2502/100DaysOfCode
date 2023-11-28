#Write a program to implement a depth-first search (DFS) algorithm..
print ("\nSubi - Day 70 of #100DaysOfCode\n") 
print("\nWrite a program to implement a depth-first search (DFS) algorithm.\n")\

def dfs(graph, start_node):

  visited = []
  stack = [start_node]

  while stack:
    node = stack.pop()
    visited.append(node)

    for neighbor in graph[node]:
      if neighbor not in visited:
        stack.append(neighbor)

  return visited

if __name__ == "__main__":
  graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
  }

  start_node = "A"

  visited = dfs(graph, start_node)

  print(visited)
  