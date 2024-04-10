
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
n, l, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
days = 0
while True:
    prev = deepcopy(arr)
    dp = [[0]*n for _ in range(n)]
    dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    cnt = 1
    lst = [[0, 0] for _ in range(cnt+1)]
    for i in range(n):
        for j in range(n):
            if not dp[i][j]:
                dp[i][j] = cnt
                q = deque([[i, j]])
                lst[cnt][0] += 1
                lst[cnt][1] += arr[i][j]
                while q:
                    x, y = q.popleft()
                    for dx, dy in dr:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and not dp[nx][ny] and l <= abs(arr[nx][ny]-arr[x][y]) <= h:
                            dp[nx][ny] = cnt
                            q.append([nx, ny])
                            lst[cnt][0] += 1
                            lst[cnt][1] += arr[nx][ny]
                lst.append([0, 0])
                cnt += 1

    av_lst = [0]*cnt
    for c in range(1, cnt):
        av_lst[c] = lst[c][1] // lst[c][0]
    for i in range(n):
        for j in range(n):
            arr[i][j] = av_lst[dp[i][j]]
    if arr == prev:
        break
    days += 1
print(days)