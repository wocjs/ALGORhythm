
import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
wsm, bsm = 0, 0

for i in range(n):
	for j in range(m):
		if not visited[i][j]:
			q = deque([[i, j]])
			visited[i][j] = 1
			cnt = 1
			while q:
				x, y = q.popleft()
				for dx, dy in dr:
					nx, ny = x+dx, y+dy
					if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[x][y] == arr[nx][ny]:
						q.append([nx, ny])
						visited[nx][ny] = 1
						cnt += 1
			if arr[i][j] == 'W':
				wsm += cnt**2
			else:
				bsm += cnt**2
print(wsm, bsm)