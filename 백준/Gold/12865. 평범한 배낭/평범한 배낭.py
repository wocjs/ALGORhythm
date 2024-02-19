# B12865
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = [[0, 0]]
for _ in range(n):
    w, v = map(int, input().split())
    lst.append([w, v])
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight, value = lst[i]
        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
print(dp[n][k])