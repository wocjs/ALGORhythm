
# B2644
import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
q = deque()
q.append([a, 0])
while q:
    now, cnt = q.popleft()
    visited[now] = 1
    if now == b:
        print(cnt)
        exit(0)
    for nxt in graph[now]:
        if not visited[nxt]:
            q.append([nxt, cnt+1])
print(-1)