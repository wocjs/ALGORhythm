
import sys
from collections import deque
input = sys.stdin.readline

INF = float('inf')
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    st, en, val = map(int, input().split())
    graph[st].append([val, en])

for i in graph:
    i.sort()
st, en = map(int, input().split())
dist = [INF] * (n + 1)
q = deque()
q.append(st)
dist[st] = 0
while q:
    now = q.popleft()
    visited[now] = 1
    for val, nxt in graph[now]:
        if val + dist[now] < dist[nxt]:
            q.append(nxt)
            dist[nxt] = val + dist[now]
print(dist[en])