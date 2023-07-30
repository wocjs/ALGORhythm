
from collections import deque

def bfs(a, b):
    q = deque()
    q.append([a, b])
    while q:
        x, y = q.popleft()
        # visited[x][y] = 1     # case 1번, 이걸 살리고
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])


n = int(input())
arr = [list(input()) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
cnt1 = 0
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited = [[0] * n for _ in range(n)]
cnt2 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1
print(cnt1, cnt2)
