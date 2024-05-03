
from collections import deque
import sys
input = sys.stdin.readline
dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
total_s = 0
total_w = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] != '#':
            s = 0
            w = 0
            if arr[i][j] == 'v':
                w += 1
            elif arr[i][j] == 'o':
                s += 1
            q = deque([[i, j]])
            visited[i][j] = 1
            while q:
                x, y = q.popleft()
                for dx, dy in dr:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] != '#':
                        if arr[nx][ny] == 'o':
                            s += 1
                        elif arr[nx][ny] == 'v':
                            w += 1
                        visited[nx][ny] = 1
                        q.append([nx, ny])
            # print(i, j, s, w)
            if s > w:
                w = 0
            else:
                s = 0
            total_s += s
            total_w += w

print(total_s, total_w)