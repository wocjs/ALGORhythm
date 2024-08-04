import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    cnt = 0   # 시간 기록
    while q:
        cnt += 1
        # fire first
        while fire and fire[0][2] < cnt:
            x, y, time = fire.popleft()
            for dx, dy in dr:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m and (arr[nx][ny] == '.' or arr[nx][ny] == '@'):
                    arr[nx][ny] = '*'
                    fire.append([nx, ny, time+1])
        while q and q[0][2] < cnt:
            # find movable spot
            x, y, time = q.popleft()
            for dx, dy in dr:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == '.' and not visited[nx][ny]:
                        q.append([nx, ny, time+1])
                        visited[nx][ny] = 1
                else:
                    return cnt


dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
T = int(input())
for tc in range(T):
    m, n = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    q = deque()
    fire = deque()
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '@':
                visited[i][j] = 1
                q.append([i, j, 0])
            elif arr[i][j] == '*':
                fire.append([i, j, 0])

    ans = bfs()
    print(ans) if ans else print('IMPOSSIBLE')