
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def getNums():
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                cnt += 1
                q = deque([[i, j]])
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    for dx, dy in dr:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                            q.append([nx, ny])
                            visited[nx][ny] = 1
    return cnt


gen = 0
while True:
    status = getNums()
    if status == 0:
        print(0)
        break
    elif status > 1:
        print(gen)
        break
    elif status == 1:
        visited = [[0]*m for _ in range(n)]
        for i in range(1, n-1):
            for j in range(1, m-1):
                if arr[i][j]:
                    for dx, dy in dr:
                        nx, ny = i+dx, j+dy
                        if arr[nx][ny] == 0:
                            visited[i][j] += 1
        for i in range(1, n-1):
            for j in range(1, m-1):
                if arr[i][j] and visited[i][j]:
                    arr[i][j] -= visited[i][j]
                    if arr[i][j] < 0:
                        arr[i][j] = 0
    gen += 1
