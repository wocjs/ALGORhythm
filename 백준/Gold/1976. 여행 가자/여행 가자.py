
import sys
input = sys.stdin.readline
def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        par[y] = x
    else:
        par[x] = y


def find(x):
    if x != par[x]:
        par[x] = find(par[x])
    return par[x]


n, m = int(input()), int(input())
par = [i for i in range(n)]
for i in range(n):
    graph = list(map(int, input().split()))
    for j in range(n):
        if graph[j] == 1:
            union(i, j)

par = [-1] + par
path = list(map(int, input().split()))
start = par[path[0]]
for i in range(1, m):
    if par[path[i]] != start:
        print("NO")
        break
else:
    print("YES")