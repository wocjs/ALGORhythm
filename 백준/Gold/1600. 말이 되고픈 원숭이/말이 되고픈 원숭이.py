
from collections import deque
import sys
input = sys.stdin.readline
hdr = [[-2, -1], [-2, 1], [-1, 2], [1, 2],
       [2, 1], [2, -1], [1, -2], [-1, -2]]
mdr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
power = int(input())
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0]*(power+1) for _ in range(m)] for _ in range(n)]
q = deque([[0, 0, 0]])
visited[0][0][0] = 1
while q:
    x, y, z = q.popleft()
    if [x, y] == [n-1, m-1]:
        print(visited[x][y][z]-1)
        exit()
    for dx, dy in mdr:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][z] and not arr[nx][ny]:
            visited[nx][ny][z] = visited[x][y][z]+1
            q.append([nx, ny, z])
    if z < power:
        for dx, dy in hdr:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][z+1] and not arr[nx][ny]:
                visited[nx][ny][z+1] = visited[x][y][z]+1
                q.append([nx, ny, z+1])
else:
    print(-1)