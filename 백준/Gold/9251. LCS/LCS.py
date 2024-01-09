lst1 = input()
lst2 = input()
n1 = len(lst1)
n2 = len(lst2)
dp = [[0] * (n2+1) for _ in range(n1+1)]

for i in range(n1 + 1):
    for j in range(n2 + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif lst1[i - 1] == lst2[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])