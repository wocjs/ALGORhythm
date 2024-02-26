# B20303
def find(x):
    if par[x] == x:
        return par[x]
    par[x] = find(par[x])
    return par[x]

def union(_a, _b):
    _a = find(_a)
    _b = find(_b)
    if _a < _b:
        _a, _b = _b, _a
    par[_a] = _b


n, m, k = map(int, input().split())
candy = [0] + list(map(int, input().split()))
par = [i for i in range(n+1)]
friend = [0] + [1] * n

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n+1):
    if i != par[i]:
        root = find(i)
        candy[root] += candy[i]
        friend[root] += friend[i]


def bag(_k):
    lst = []
    for i in range(1, n+1):
        if par[i] == i:
            lst.append([friend[i], candy[i]])
    _n = len(lst)
    dp = [[0] * _k for _ in range(_n)]
    for i in range(_n):
        w, v = lst[i]
        for j in range(1, _k):
            if w > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
    print(dp[-1][-1])

bag(k)
