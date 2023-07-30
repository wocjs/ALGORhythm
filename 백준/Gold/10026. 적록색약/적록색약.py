import sys
from collections import deque


def bfs(i, j):
    visited[i][j] = 1
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for dr in range(4):
            nx = x + dx[dr]
            ny = y + dy[dr]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])


n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

cnt = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

cnt = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1
print(cnt)