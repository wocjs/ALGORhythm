
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(n-1):
	a, b = map(int,input().split())
	arr[a].append(b)
	arr[b].append(a)
visited = [0] * (n + 1)
q = deque([1])
visited[1] = 1
while q:
	now = q.popleft()
	for nxt in arr[now]:
		if not visited[nxt]:
			visited[nxt] = now
			q.append(nxt)
print(*visited[2:])