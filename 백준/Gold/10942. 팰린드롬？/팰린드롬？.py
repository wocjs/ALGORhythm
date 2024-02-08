
# B10942
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

dp = [[0]*n for _ in range(n)]

for i in range(n):
	dp[i][i] = 1

for i in range(n-1):
	if arr[i] == arr[i+1]:
		dp[i][i+1] = 1
	else:
		dp[i][i+1] = 0
for cnt in range(n-2):
	for i in range(n-2-cnt):
		j = i + 2 + cnt
		# 점화식
		if arr[i] == arr[j] and dp[i+1][j-1]:
			dp[i][j] = 1

m = int(input())
for _ in range(m):
	i, j = map(int, input().split())
	print(dp[i-1][j-1])