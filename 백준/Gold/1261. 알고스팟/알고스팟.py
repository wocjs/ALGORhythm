
import sys
import heapq

input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

q = []
heapq.heappush(q, [0, 0, 0])    # cost, x, y
dist = [[float('inf')]*m for _ in range(n)]
dist[0][0] = 0

while q:
    cost, x, y = heapq.heappop(q)

    # prunning
    if cost > dist[x][y]:
        continue

    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            # 현재 x, y에서 값 + nx, ny에 들어가 있는 값
            nxt_cost = cost + arr[nx][ny]
            if nxt_cost < dist[nx][ny]:
                dist[nx][ny] = nxt_cost
                heapq.heappush(q, [nxt_cost, nx, ny])
print(dist[n-1][m-1])
