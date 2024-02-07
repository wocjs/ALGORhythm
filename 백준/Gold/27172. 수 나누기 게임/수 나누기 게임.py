# B27172
# 에라토스테네스의 체
n = int(input())
arr = list(map(int, input().split()))
# arr.sort()
st = set(arr)
mx = max(st)
dp = [0] * (mx+1)
for nm in arr:
    if nm == mx:
        continue
    tmp = nm * 2
    while tmp < mx+1:
        if tmp in st:
            dp[nm] += 1
            dp[tmp] -= 1
        tmp += nm
for i in arr:
    print(dp[i], end=' ')
print()