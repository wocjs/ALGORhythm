import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
	n1, n2, val = map(int, input().split())
	graph[n1].append([val, n2])
	graph[n2].append([val, n1])
for i in graph:
	i.sort()
n1, n2 = map(int, input().split())

def find(st):
	dist = [INF] * (v+1)
	q = deque()
	q.append([0, st])
	dist[st] = 0
	while q:
		val, now = q.popleft()
		if dist[now] < val:
			continue
		for i in graph[now]:
			nxtval = val + i[0]
			if dist[i[1]] > nxtval:
				dist[i[1]] = nxtval
				q.append([nxtval, i[1]])
	return dist

nmdist = find(1)
n1dist = find(n1)
n2dist = find(n2)

ans = min(nmdist[n1]+n1dist[n2]+n2dist[v], nmdist[n2]+n2dist[n1]+n1dist[v])
if ans == INF:
	print(-1)
else:
	print(ans)