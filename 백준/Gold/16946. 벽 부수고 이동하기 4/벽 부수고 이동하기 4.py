# B16946
import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j):
    q = deque([[i, j]])
    cnt = 1
    while q:
        x, y = q.popleft()
        groupMap[x][y] = g_nm
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0<= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])
                cnt += 1
    return cnt


n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
groupMap = [[0]*m for _ in range(n)]
g_nm = 1
dr = [[-1, 0], [1, 0], [0, 1], [0, -1]]
dic = {}
dic[0] = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            visited[i][j] = 1
            w = bfs(i, j)
            dic[g_nm] = w
            g_nm += 1

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            add_lst = set()
            x, y = i, j
            for dx, dy in dr:
                nx = x + dx
                ny = y + dy
                if 0<= nx < n and 0 <= ny < m:
                    add_lst.add(groupMap[nx][ny])
            for addidx in add_lst:
                # print(addidx)
                arr[i][j] += dic[addidx]
                arr[i][j] %= 10

for i in range(n):
    for j in range(m):
        print(arr[i][j], end='')
    print()