import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = float("inf")
mx = 256
for i in range(n):
    mx = max(mx, max(arr[i]))
for floor in range(257):
    mn_cnt, mx_cnt = 0, 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > floor:
                mx_cnt += arr[i][j] - floor
            else:
                mn_cnt += floor - arr[i][j]
    if mx_cnt + b >= mn_cnt:
        if (mx_cnt * 2) + mn_cnt <= ans:
            ans = (mx_cnt * 2) + mn_cnt
            idx = floor
print(ans, idx)