
# B7579
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
byte = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [[0]*(sum(cost)+1) for _ in range(n+1)]
res = sum(cost)

for i in range(1, n+1):
    b = byte[i]
    c = cost[i]
    for j in range(sum(cost)+1):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + b)
        if dp[i][j] >= k:
            res = min(res, j)   # 현재 j와 비교
print(res)