
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

ans = 0
for i in range(n):
	for j in range(m):
		if not visited[i][j]:
			ans += 1
			q = deque([[i, j]])
			visited[i][j] = 1
			while q:
				x, y = q.popleft()
				# 가로
				if arr[x][y] == '-':
					dr = [[0, -1], [0, 1]]
				else:
					dr = [[-1, 0], [1, 0]]
				for dx, dy in dr:
					nx, ny = x+dx, y+dy
					if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[x][y] == arr[nx][ny]:
						visited[nx][ny] = 1
						q.append([nx, ny])
print(ans)