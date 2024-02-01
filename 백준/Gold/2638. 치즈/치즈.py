
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while True:
    visited = [[0]*m for _ in range(n)]
    q = deque([[0, 0]])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # [nx][ny]가 공기면 -> 큐 추가, 방문처리
                if arr[nx][ny] == 0 and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                # [nx][ny]가 치즈면 -> 접촉면 갯수 하나 추가
                elif arr[nx][ny] == 1:
                    visited[nx][ny] += 1
    # 외부 공기 bfs 다돌았으니 없앨 치즈 체크
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] >= 2:
                arr[i][j] = 0
    cnt += 1
    done = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                done = 0
                break
        if not done:
            break
    if done:
        break
print(cnt)