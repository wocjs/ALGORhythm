
def find(d, fr, to):
    if d <= 1:
        return m[d][fr][to]
    
    m.setdefault(d, [[0] * n for _ in range(n)])
    if m[d][fr][to]:
        return m[d][fr][to]

    mid = d // 2
    if d % 2:
        oth = mid + 1
    else:
        oth = mid

    # 플로이드 워셜처럼 fr-to = fr-k + k-to
    for k in range(n):
        m[d][fr][to] += find(mid, fr, k) * find(oth, k, to)
        m[d][fr][to] %= MOD

    return m[d][fr][to]


d = int(input())
MOD = 1000000007
n = 8
m = {}
m[1] = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
]


print(find(d, 0, 0))
