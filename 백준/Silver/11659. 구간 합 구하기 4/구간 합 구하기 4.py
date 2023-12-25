
n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = arr[0]
for i in range(1, n):
	dp[i] = dp[i-1] + arr[i]
# print(dp)
for _ in range(m):
	i, j = map(int, input().split())
	print(dp[j-1] - dp[i-2])