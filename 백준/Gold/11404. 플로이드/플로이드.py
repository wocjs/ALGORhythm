# B11404
import sys
input = sys.stdin.readline
INF = float('inf')

v = int(input())
e = int(input())

# init floyd-warshall graph
graph = [[INF]*(v+1) for _ in range(v+1)]
for i in range(v+1):
	graph[i][i] = 0

for _ in range(e):
	a, b, c = map(int, input().split())
	graph[a][b] = min(graph[a][b], c)

# implement
for k in range(1, v+1):
	for i in range(1, v+1):
		for j in range(1, v+1):
			graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, v+1):
	for j in range(1, v+1):
		print(graph[i][j], end=' ') if graph[i][j] != INF else print(0, end=' ')
	print()