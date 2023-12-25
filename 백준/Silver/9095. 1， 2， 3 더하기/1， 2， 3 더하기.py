
'''
(1) (N - 1) 에서 1 더하기 -> N-1을 만드는 경우의 수와 동일 = dp[N-1]
(2) (N - 2) 에서 2 더하기 -> N-2을 만드는 경우의 수와 동일 = dp[N-2]
(3) (N - 3) 에서 3 더하기 -> N-3을 만드는 경우의 수와 동일 = dp[N-3]
'''
'''
n = 1 -> 1
n = 2 -> 2
n = 3 -> 4
'''

import sys
input = sys.stdin.readline

t = int(input())
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 12):
	dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for tc in range(t):
	n = int(input())
	print(dp[n])
	