n = int(input())
dp = [0, 1]
for i in range(2, n + 1):
	mn = 4
	j = 1
	while (j**2) <= i:
		mn = min(mn, dp[i - j**2])
		j += 1
	dp.append(mn + 1)
#	print(dp)
print(dp[n])