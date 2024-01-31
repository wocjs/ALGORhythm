
# B2206
from collections import deque
import sys
input = sys.stdin.readline
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]    # [i, j]마다 [안부술때, 부술때]여기까지 거리를 저장
q = deque([[0, 0, 0]])  # x, y, used
visited[0][0][0] = 1
while q:
    x, y, used = q.popleft()
    if x == n-1 and y == m-1:
        print(visited[x][y][used])
        exit()
    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            # 있을 때 벽
            if not used and arr[nx][ny]:
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append([nx, ny, 1])
            # 빈공간에 방문 안함
            elif not visited[nx][ny][used] and arr[nx][ny] == 0:
                visited[nx][ny][used] = visited[x][y][used] + 1
                q.append([nx, ny, used])
print(-1)
