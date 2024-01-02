
from collections import deque
def find(node):
	q = deque()
	q.append(node)
	visited[node] = 1
	while q:
		now = q.popleft()
		for i in graph[now]:
			if not visited[i]:
				visited[i] = visited[now] + 1
				q.append(i)
		

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
	e1, e2 = map(int, input().split())
	graph[e1].append(e2)
	graph[e2].append(e1)
# print(graph)	# [[], [3, 4], [3], [1, 4, 2], [1, 5, 3], [4]]

res = []
for i in range(1, n + 1):
	visited = [0] * (n + 1)
	find(i)
	res.append(sum(visited))
print(res.index(min(res)) + 1)