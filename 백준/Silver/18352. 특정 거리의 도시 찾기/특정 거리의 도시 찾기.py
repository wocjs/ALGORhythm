import sys
import heapq
input = sys.stdin.readline
inf = float('inf')

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [inf]*(n+1)
dist[x] = 0
q = []
heapq.heappush(q, x)
while q:
    now = heapq.heappop(q)
    if dist[now] > k:
        continue
    for nxt in graph[now]:
        if dist[nxt] > dist[now]+1:
            dist[nxt] = dist[now]+1
            heapq.heappush(q, nxt)
ans = []
for i in range(1, n+1):
    if dist[i] == k:
        ans.append(i)
if ans:
    for a in ans:
        print(a)
else:
    print(-1)