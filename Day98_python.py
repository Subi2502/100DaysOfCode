#Write a program to find the longest path in a directed acyclic graph (DAG).
print ("\nSubi - Day 98 of #100DaysOfCode\n") 
print("\nWrite a program to find the longest path in a directed acyclic graph (DAG)\n")

def topologicalSortUtil(v):
	global Stack, visited, adj
	visited[v] = True

	for i in adj[v]:
		if (not visited[i[0]]):
			topologicalSortUtil(i[0])
	Stack.append(v)
	
def longestPath(s):
	global Stack, visited, adj, V
	dist = [-10**9 for i in range(V)]

	for i in range(V):
		if (visited[i] == False):
			topologicalSortUtil(i)
	dist[s] = 0

	while (len(Stack) > 0):
		u = Stack[-1]
		del Stack[-1]

		if (dist[u] != 10**9):
			for i in adj[u]:
				if (dist[i[0]] < dist[u] + i[1]):
					dist[i[0]] = dist[u] + i[1]

	for i in range(V):
		print("INF ",end="") if (dist[i] == -10**9) else print(dist[i],end=" ")

if __name__ == '__main__':
	V, Stack, visited = 6, [], [False for i in range(7)]
	adj = [[] for i in range(7)]

	adj[0].append([2, 4])
	adj[0].append([4, 1])
	adj[1].append([7, 2])
	adj[1].append([3, 9])
	adj[2].append([9, 5])
	adj[2].append([6, 3])
	adj[2].append([8, 8])
	adj[3].append([6, 4])
	adj[3].append([1, -6])
	adj[4].append([5, -4])

	s = 1
	print("Following are longest distances from source vertex ",s)
	longestPath(s)