n, k = map(int, input().split())
arr = list(map(int, input().split()))
st, en = 0, 0

dp = [0] * (max(arr) + 1)
ans = 0
# print(dp)
while st < n:
    if dp[arr[st]] < k:
        dp[arr[st]] += 1
        st += 1
    else:
        dp[arr[en]] -= 1
        en += 1
    ans = max(ans, st - en)
print(ans)