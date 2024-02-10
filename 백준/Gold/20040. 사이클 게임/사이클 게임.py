
# B20040
import sys
input = sys.stdin.readline
def find(x):
    if par[x] == x:
        return x
    return find(par[x])

def union(a, b, i):
    global ans
    a = find(a)
    b = find(b)
    if a != b:
        par[max(a, b)] = min(a, b)
    # a == b이고, ans == 0일 때(최초의 사이클 형성때)
    elif ans == 0:
        ans = i+1

n, m = map(int, input().split())
par = [i for i in range(n)]
ans = 0
for i in range(m):
    n1, n2 = map(int, input().split())
    # 차례를 인자로 같이 전달
    union(n1, n2, i)
print(ans)