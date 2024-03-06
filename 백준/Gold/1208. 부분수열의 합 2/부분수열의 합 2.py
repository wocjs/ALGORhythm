
# B1208
import sys
from itertools import combinations
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


def getSm(_arr, smArr):
    for i in range(1, len(arr)+1):
        for c in combinations(_arr, i):
            smArr.append(sum(c))
    smArr.sort()
    pass


def getNm(_arr, find):
    return bisect_right(_arr, find) - bisect_left(_arr, find)
    pass


n, s = map(int, input().split())
arr = list(map(int, input().split()))

l, r = arr[:n//2], arr[n//2:]
lSm, rSm = [], []

getSm(l, lSm)
getSm(r, rSm)
ans = 0

for _l in lSm:
    find = s - _l
    ans += getNm(rSm, find)

ans += getNm(lSm, s)
ans += getNm(rSm, s)

print(ans)