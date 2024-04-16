
from collections import deque
import sys
input = sys.stdin.readline
dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
ans = []
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j]:
            q = deque([[i, j]])
            cnt = 1
            visited[i][j] = 1
            while q:
                x, y = q.popleft()
                for dx, dy in dr:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny]:
                        q.append([nx, ny])
                        visited[nx][ny] = 1
                        cnt += 1
            ans.append(cnt)
if ans:
    print(len(ans))
    print(max(ans))
else:
    print(0)
    print(0)