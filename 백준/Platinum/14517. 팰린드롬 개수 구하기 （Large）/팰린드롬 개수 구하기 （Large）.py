
import sys
sys.setrecursionlimit(10**6)
def find(l, r):
    if dp[l][r]:
        return dp[l][r]
    if l == r:
        return 1
    elif l > r:
        return 0
    dp[l][r] = (find(l, r-1) + find(l+1, r) - find(l+1, r-1)) % mod
    if s[l] == s[r]:
        dp[l][r] = (dp[l][r] + find(l+1, r-1) + 1) % mod
    return dp[l][r]


s = input()
mod = 10007
dp = [[0]*len(s) for _ in range(len(s))]
print(find(0, len(s)-1))