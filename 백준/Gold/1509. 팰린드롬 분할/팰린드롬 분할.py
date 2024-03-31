
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline().rstrip

s = input()
l = len(s)

dp = [2500] * (l+1)
dp[-1] = 0

is_p = [[0]*l for _ in range(l)]

# 길이 1짜리 팰린드롬
for i in range(l):
    is_p[i][i] = 1

# 길이 2짜리 팰린드롬
for i in range(1, l):
    if s[i] == s[i-1]:
        is_p[i-1][i] = 1

# 길이 3 ~ l짜리 팰린드롬
for _l in range(3, l+1):
    for st in range(l-_l+1):
        en = st + _l - 1
        # 처음과 끝이 같고 그 사이가 팰린드롬이면
        if s[st] == s[en] and is_p[st+1][en-1]:
            is_p[st][en] = 1

for en in range(l):
    for st in range(en+1):
        if is_p[st][en]:
            dp[en] = min(dp[en], dp[st-1] + 1)
        else:
            dp[en] = min(dp[en], dp[en-1] + 1)
print(dp[l-1])