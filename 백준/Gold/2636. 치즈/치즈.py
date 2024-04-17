
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
prev = 0
turn = 0

while True:
    cheese = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                cheese += 1
    if cheese == 0:
        break
    prev = cheese
    visited = [[0]*m for _ in range(n)]
    cheeseq = []
    q = deque([[0, 0]])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dr:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    cheeseq.append([nx, ny])
                elif arr[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1

    for x, y in cheeseq:
        arr[x][y] = 0
    turn += 1
print(turn)
print(prev)