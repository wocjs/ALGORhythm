
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def inRange(x, y, cnt):
    return 0 <= x < n and 0 <= y < m and arr[x][y] < cnt


def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for dx, dy in dr:
            nx, ny = x+dx, y+dy
            if inRange(nx, ny, arr[x][y]):
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

print(dfs(0, 0))
