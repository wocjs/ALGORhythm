
# B17144
from collections import deque
import sys
input = sys.stdin.readline
n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1):
    if arr[i][0] == -1 and arr[i+1][0] == -1:
        up, down = i, i+1
        break

# Spread
def spread():
    dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    dust = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                dust.append([i, j])
    _arr = [[0]*m for _ in range(n)]
    while dust:
        x, y = dust.popleft()
        cnt = 0
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != -1:
                _arr[nx][ny] += arr[x][y] // 5
                cnt += 1
        arr[x][y] -= (arr[x][y] // 5) * cnt
    for i in range(n):
        for j in range(m):
            arr[i][j] += _arr[i][j]

def upC():
    for i in range(up-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    for j in range(m-1):
        arr[0][j] = arr[0][j+1]
    for i in range(up):
        arr[i][m-1] = arr[i+1][m-1]
    for j in range(m-1, 1, -1):
        arr[up][j] = arr[up][j-1]
    arr[up][1] = 0

def downC():
    for i in range(down+1, n-1):
        arr[i][0] = arr[i+1][0]
    for j in range(m-1):
        arr[n-1][j] = arr[n-1][j+1]
    for i in range(n-1, down, -1):
        arr[i][m-1] = arr[i-1][m-1]
    for j in range(m-1, 1, -1):
        arr[down][j] = arr[down][j-1]
    arr[down][1] = 0

for _ in range(t):
    spread()
    upC()
    downC()
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] > 0:
            ans += arr[i][j]
print(ans)