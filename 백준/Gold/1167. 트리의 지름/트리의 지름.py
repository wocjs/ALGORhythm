
#B1167
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(1, n+1):
	lst = list(map(int, input().split()))
	for i in range(1, len(lst)-1, 2):
		arr[lst[0]].append([lst[i], lst[i+1]])
		
def bfs(node):
	visited = [0] * (n+1)
	q = deque([node])
	visited[node] = 1
	mx = [0, 0]
	while q:
		now = q.popleft()
		for nxt, val in arr[now]:
			if not visited[nxt]:
				visited[nxt] = visited[now] + val
				q.append(nxt)
				if mx[0] < visited[nxt]:
					mx = [visited[nxt], nxt]
					
	return mx
# 임의의 노드에서 제일 멀리 이동한 다음, 
# 그 노드에서 다시 BFS 돌면 그 두 점이 가장 먼 두 노드임
_, node = bfs(1)
val, _ = bfs(node)
print(val-1)