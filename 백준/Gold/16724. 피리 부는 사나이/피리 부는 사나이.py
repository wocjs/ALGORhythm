
# B16724
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        par[b] = a
    else:
        par[a] = b


n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
par = [i for i in range(n*m)]
dr = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1]
}


# 2차원 행렬에서 union-find로 계산하기 위해 1차원으로 변경
for now in range(n*m):
    x, y = now // m, now % m
    dx, dy = dr[arr[x][y]]
    nx, ny = x + dx, y + dy
    nxt = nx*m + ny
    union(now, nxt)
# 끝나고 덜된놈들 초기화
for i in range(1, n*m):
    par[i] = find(i)
# print(par[0], end='\t')
# for i in range(1, n*m):
#     if i % m == 0:
#         print()
#     print(par[i], end='\t')
# print("\n##########")
print(len(set(par)))