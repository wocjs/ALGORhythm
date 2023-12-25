
from itertools import combinations
import sys
input = sys.stdin.readline

def dit(a, b):
    dist = 0
    for i, j in zip(a, b):
        if i != j:
            dist += 1
    return dist


T = int(input())
for tc in range(T):
    n = int(input())
    mbti = input().rstrip().split()

    if n > 32:
        print(0)
        continue

    ans = 13
    case = combinations(mbti, 3)
    for a, b, c in case:
        dist = 0
        dist += dit(a, b)
        dist += dit(b, c)
        dist += dit(c, a)
        ans = min(ans, dist)
    print(ans)