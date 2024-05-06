import sys
sys.setrecursionlimit(10**7)
from bisect import bisect_right
input = sys.stdin.readline


def find(x):
    if par[x] != x:
        par[x] = find(par[x])
    return par[x]


def union(a, b):
    if b >= m:
        return
    a = find(a)
    b = find(b)
    par[a] = b


n, m, k = map(int, input().split())
cards = [*map(int, input().split())]
chulsoo = [*map(int, input().split())]
par = [i for i in range(m)]
cards.sort()
for i in chulsoo:
    idx = bisect_right(cards, i)
    idx = find(idx)
    print(cards[idx])
    union(idx, idx+1)
