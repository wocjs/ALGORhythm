from collections import deque
n= int(input())

arr = [list(map(int, input().strip())) for _ in range(n)]
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[0] * n for _ in range(n)]
ans = []
for i in range(n):
	for j in range(n):
		if arr[i][j] and not visited[i][j]:
			cnt = 1
			visited[i][j] = 1
			q = deque()
			q.append([i, j])
			while q:
				x, y = q.popleft()
				for dx, dy in dr:
					nx, ny = x + dx, y + dy
					if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] and not visited[nx][ny]:
						cnt += 1
						visited[nx][ny] = 1
						q.append([nx, ny])
			ans.append(cnt)
print(len(ans))
ans.sort()
for i in ans:
	print(i)