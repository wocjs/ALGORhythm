import sys
from collections import deque
input = sys.stdin.readline
dr = [[-1, -1], [-1, 0], [-1, 1],
      [0, -1], [0, 1],
      [1, -1], [1, 0], [1, 1]]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
shark = deque()
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            visited[i][j] = 1
            shark.append([i, j])
            while shark:
                x, y = shark.popleft()
                for dx, dy in dr:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
                        if visited[nx][ny] == 0:
                            visited[nx][ny] = visited[x][y] + 1
                            shark.append([nx, ny])
                        elif visited[nx][ny] - visited[x][y] > 1:
                            visited[nx][ny] = visited[x][y] + 1
                            shark.append([nx, ny])
mx = 0
for lst in visited:
    mx = max(mx, max(lst))
print(mx-1)