
# B14938
import sys
input = sys.stdin.readline
INF = float('inf')

n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))
graph = [[INF]*(n+1) for _ in range(n+1)]

# init
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = min(graph[a][b], l)
    graph[b][a] = min(graph[b][a], l)

for i in range(n+1):
    graph[i][i] = 0


# Floyd-Warshall
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

mx = 0
for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            tmp += item[j]
    mx = max(mx, tmp)
print(mx)