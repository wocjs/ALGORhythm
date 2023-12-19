
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = deque()
q.append((0, 0))

while q:
	x, y = q.popleft()
	for dx, dy in dr:
		nx, ny = x + dx, y + dy
		if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
			q.append((nx, ny))
			visited[nx][ny] = visited[x][y] + 1
print(visited[n-1][m-1])