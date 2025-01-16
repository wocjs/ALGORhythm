
import sys, math
input = sys.stdin.readline


def dfs(x):
    visited[x] = True
    for next, power in tmp[x]:
        if not visited[next]:
            arr[next] = [x, power]
            dfs(next)


def lca(j, w):
    for i in range(int(math.log2(n)), -1, -1):
        if spareTable[i][j][1] <= w and spareTable[i][j][0] != 0:
            w -= spareTable[i][j][1]
            j = spareTable[i][j][0]
    return j


n = int(input().rstrip())
ant = [0] + [int(input().rstrip()) for _ in range(n)]
arr = [[] for _ in range(n + 1)]
tmp = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().rstrip().split())
    tmp[b].append([a, c])
    tmp[a].append([b, c])

visited = [False] * (n + 1)
dfs(1)
arr[1] = [1, 0]

spareTable = [[[0, 0] for _ in range(n + 1)] for _ in range(int(math.log2(n)) + 1)]
for i in range(1, n + 1):
    spareTable[0][i] = arr[i]

for k in range(1, int(math.log2(n)) + 1):
    for i in range(1, n + 1):
        next, power = spareTable[k-1][i]
        spareTable[k][i] = [spareTable[k-1][next][0], power+spareTable[k-1][next][1]]

for i in range(1, n + 1):
    print(lca(i, ant[i]))