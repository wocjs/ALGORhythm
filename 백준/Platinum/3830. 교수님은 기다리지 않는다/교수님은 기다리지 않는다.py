import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def union(a, b, w):
    val[a] -= w
    par[a] = b
    parVal[a] = val[b]


def find(x):
    if par[x] != x:
        p, pv = par[x], parVal[x]
        par[x] = find(p)
        val[x] += val[p] - pv
        parVal[x] = val[par[x]]
    return par[x]


while True:
    n, m = map(int, input().split())
    if not n:
        break
    par = [i for i in range(n+1)]
    val = [0] * (n+1)
    parVal = [0] * (n+1)

    for _ in range(m):
        q = input().split()
        if q[0] == '?':
            a, b = map(int, q[1:])
            if find(a) == find(b):
                print(val[b]-val[a])
            else:
                print("UNKNOWN")
        else:
            a, b, w = map(int, q[1:])
            if find(a) != find(b):
                union(par[a], par[b], w-val[b]+val[a])
