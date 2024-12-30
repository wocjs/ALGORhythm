
import sys
input = sys.stdin.readline

def find(x, y):
    for dx, dy in dr:
        nx = x+dx
        ny = y+dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if graph[nx][ny] == 'x' or done[nx][ny]:
            continue
        done[nx][ny] = 1
        if not link[nx][ny] or find(*link[nx][ny]):
            link[nx][ny] = [x, y]
            return 1
    return 0

t = int(input())
dr = [[-1, -1], [0, -1], [1, -1], [-1, 1], [0, 1], [1, 1]]
for _ in range(t):
    n, m = map(int, input().split())
    graph = [input() for _ in range(n)]
    link = [[0]*m for _ in range(n)]
    ans = n * m
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'x':
                ans -= 1
                continue
            if not j % 2:
                continue
            done = [[0]*m for _ in range(n)]
            ans -= find(i, j)
    print(ans)