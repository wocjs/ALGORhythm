n = int(input())
xlst, ylst, zlst = [], [], []
for i in range(n):
    x, y, z = map(int, input().split())
    xlst.append((x, i))
    ylst.append((y, i))
    zlst.append((z, i))
xlst.sort()
ylst.sort()
zlst.sort()

edge = []
for lst in xlst, ylst, zlst:
    for i in range(1, n):
        w1, n1 = lst[i - 1]
        w2, n2 = lst[i]
        edge.append((abs(w1 - w2), n1, n2))
edge.sort()


# Kruskal
def find(x):
    if x != par[x]:
        par[x] = find(par[x])
    return par[x]


def union(x, y):
    rootx = find(x)
    rooty = find(y)
    if rootx < rooty:
        par[rooty] = rootx
    else:
        par[rootx] = rooty


par = [i for i in range(n + 1)]
cnt = 0
ans = 0

for i in range(n*3):
    w, a, b = edge[i]
    if find(a) == find(b):
        continue
    union(a, b)
    cnt += 1
    ans += w
    if cnt == n-1:
        print(ans)
        exit(0)
