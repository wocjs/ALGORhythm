
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
# 0 = -, 1 = /, 2 = |

dp[0][1] = [1,0,0] # 시자
for i in range(n):
	for j in range(2, n):
		if i == 0:	# init
			if not arr[i][j]:
				dp[i][j] = [1, 0, 0]
				continue
			else:
				break
			
		
		if not arr[i][j] and not arr[i-1][j] and not arr[i][j-1]:
			dp[i][j][1] = sum(dp[i-1][j-1])
		if not arr[i][j]:
			dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
			dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]
# for i in dp:
# 	print(i)
print(sum(dp[n-1][n-1]))