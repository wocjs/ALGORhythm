
from bisect import bisect_left
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

dp = [1]
x = [arr[0][1]]
res = [1]

for v in range(1, n):
    _i, val = arr[v]
    if x[-1] < val:
        dp.append(dp[-1]+1)
        x.append(val)
        res.append(len(dp))
    else:
        idx = bisect_left(x, val)
        x[idx] = val
        res.append(idx+1)

# print(dp)
# print(x)
# print(res)

ans = []
v = dp[-1]
pt = n - 1
while pt >= 0:
    if res[pt] == v:
        v -= 1
    else:
        ans.append(arr[pt][0])
    pt -= 1

print(len(ans))
for i in ans[::-1]:
    print(i)