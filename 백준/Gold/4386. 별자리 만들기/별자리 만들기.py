# B4386
import sys
import math
input = sys.stdin.readline


def cal_dst(a, b):
    return round(math.sqrt(abs(arr[a][0] - arr[b][0])**2 +
                           abs(arr[a][1] - arr[b][1])**2), 2)

def find(x):
    if x == par[x]:
        return par[x]
    return find(par[x])


def union(a, b):  # always b is bigger
    a = find(a)
    b = find(b)
    par[b] = a


n = int(input())
arr = [[0, 0]]
for i in range(n):
    a, b = map(float, input().split())
    arr.append([a, b])
dist = []
for i in range(1, n+1):
    for j in range(i, n+1):
        if i == j:
            continue
        dist.append([cal_dst(i, j), i, j])
dist.sort()
# 이때 dist의 두 간선은 항상 오름차순으로 저장됨
par = [i for i in range(n+1)]
ans = 0
for e in dist:
    cost, a, b = e
    if find(a) != find(b):
        union(a, b)
        ans += cost
print(ans)