
from collections import deque
import sys
input = sys.stdin.readline


# 섬의 개수를 구하고 섬마다 번호를 표시하는 bfs
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    maps[x][y] = mark

    while q:
        x, y = q.popleft()

        for dx, dy in dr:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    q.append((nx, ny))
                    maps[nx][ny] = mark
                    visited[nx][ny] = True


# 섬 사이 최단거리
def bfs2(island):
    q = deque()
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j] == island:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in dr:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] and maps[nx][ny] != island:  # 다른 섬과 만났을 경우
                    return dist[x][y]
                if maps[nx][ny] == 0 and dist[nx][ny] == -1:  # 물이고 아직 건너지 않은 곳일 경우
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))


n = int(input())
dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

mark = 1  # 섬 번호
for x in range(n):
    for y in range(n):
        if maps[x][y] == 1 and not visited[x][y]:
            bfs(x, y)
            mark += 1

res = n ** 2
for island in range(1, mark):
    res = min(res, bfs2(island))

print(res)