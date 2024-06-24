
n, k = map(int, input().split())
arr = [0] + [1] * n
cnt = 0
for i in range(2, n+1):
    nm = i
    while nm <= n:
        if arr[nm]:
            arr[nm] = 0
            cnt += 1
        nm += i
        if cnt == k:
            print(nm-i)
            exit()