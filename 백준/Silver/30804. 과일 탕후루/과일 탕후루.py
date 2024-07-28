
import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
l, r, cnt = 0, 0, 0
info = defaultdict(int)
ans = 0

while r < n:
    if info[arr[r]] == 0:
        cnt += 1
    info[arr[r]] += 1

    while cnt > 2:
        info[arr[l]] -= 1
        if info[arr[l]] == 0:
            cnt -= 1
        l += 1
    ans = max(ans, r-l+1)
    r += 1

print(ans, end='\n\n')