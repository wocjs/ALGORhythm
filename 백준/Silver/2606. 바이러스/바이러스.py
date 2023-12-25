n = int(input())
e = int(input())
par = [i for i in range(n+1)]


def find(x):
    if x != par[x]:
        par[x] = find(par[x])
    return par[x]


def union(_a, _b):
    ra = find(_a)
    rb = find(_b)
    if ra < rb:
        par[rb] = ra
    else:
        par[ra] = rb


for _ in range(e):
    a, b = map(int, input().split())
    union(a, b)
cnt = 0
for i in range(2, n + 1):
    if find(par[i]) == 1:
        cnt += 1
print(cnt)
