n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 0
ans = 0
for i in range(n-1, -1, -1):
    if arr[i] > cnt:
        ans += 1
        cnt = arr[i]
print(ans)