n, k = map(int, input().split())
arr = list(map(int, input().split()))
sm = sum(arr[0:k])
ans = sm
for i in range(1, n - k + 1):
    sm -= arr[i - 1]
    sm += arr[i + k - 1]
    ans = max(sm, ans)
print(ans)
