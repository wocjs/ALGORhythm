# B10775
import sys
input = sys.stdin.readline

def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]


def union(a, b):
    b = find(b)
    par[a] = b


n = int(input())
m = int(input())
par = [i for i in range(n+1)]

for cnt in range(m):
    plane = find(int(input()))
    if plane == 0:
        print(cnt)
        break
    union(plane, plane-1)
else:
    print(n)