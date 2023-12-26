
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
idx = k-1
now = 0
cnt = 0
while now != n:
    if arr[idx] > (n-now):
        idx -= 1
        continue
    now += arr[idx]
    cnt += 1
print(cnt)
