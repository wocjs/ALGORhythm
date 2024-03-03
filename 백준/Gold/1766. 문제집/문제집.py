# B1766
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indeg = [0] * (n+1)
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indeg[b] += 1
q = deque()
ans = []
for i in range(1, n+1):
    if indeg[i] == 0:
        q.append(i)
        break
while q:
    now = q.popleft()
    ans.append(now)
    visited[now] = 1
    for nxt in graph[now]:
        indeg[nxt] -= 1
    for i in range(1, n+1):
        if indeg[i] == 0 and not visited[i]:
            q.append(i)
            break
print(*ans)