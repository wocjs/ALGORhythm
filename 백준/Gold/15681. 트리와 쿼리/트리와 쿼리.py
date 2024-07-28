
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def cntSubTrNds(current):
    size[current] = 1
    for node in graph[current]:
        if not size[node]:  # 미방문 == 자식만 볼 수 있음
            cntSubTrNds(node)
            size[current] += size[node]


n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
size = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cntSubTrNds(r)

for _ in range(q):
    i = int(input())
    print(size[i])