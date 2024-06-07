
import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [1]
x = [arr[0]]
res = [1]
for i in range(1, n):
    if arr[i] > x[-1]:
        x.append(arr[i])
        dp.append(dp[-1] + 1)
        res.append(len(dp))
    else:
        idx = bisect_left(x, arr[i])
        x[idx] = arr[i]
        res.append(idx+1)
print(dp[-1])