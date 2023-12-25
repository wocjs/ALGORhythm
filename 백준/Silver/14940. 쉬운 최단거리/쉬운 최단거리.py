
from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dp = [[0] * m for _ in range(n)]
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(n):
	for j in range(m):
		if arr[i][j] == 2:
			q.append([i, j])
			while q:
				x, y = q.popleft()
				for dx, dy in dr:
					nx, ny = x + dx, y + dy
					if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not dp[nx][ny]:
						dp[nx][ny] = dp[x][y] + 1
						q.append([nx, ny])
			dp[i][j] = 0
			break
for i in range(n):
	for j in range(m):
		if arr[i][j] != 0 and dp[i][j] == 0:
			dp[i][j] = -1
		if arr[i][j] == 2:
			x, y = i, j
dp[x][y] = 0
for i in dp:
	print(*i)