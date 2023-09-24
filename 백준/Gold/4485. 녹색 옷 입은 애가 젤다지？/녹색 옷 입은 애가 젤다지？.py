
import heapq
import sys

input = sys.stdin.readline

dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
inf = 1e6
cnt = 0
while True:
    n = int(input())
    if n == 0:
        break
    cnt += 1
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[inf] * n for _ in range(n)]

    q = []
    heapq.heappush(q, [arr[0][0], 0, 0])
    dist[0][0] = 0
    while q:
        cost, x, y = heapq.heappop(q)

        if x == y == n - 1:
            print(f"Problem {cnt}: {dist[x][y]}")
            break
        for dx, dy in dr:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                nxt_cost = cost + arr[nx][ny]
                if dist[nx][ny] > nxt_cost:
                    dist[nx][ny] = nxt_cost
                    heapq.heappush(q, [nxt_cost, nx, ny])
