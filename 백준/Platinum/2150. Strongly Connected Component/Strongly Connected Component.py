
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
_graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    _graph[b].append(a)


def dfs(now, visited, stack):
    visited[now] = 1
    for nxt in graph[now]:
        if not visited[nxt]:
            dfs(nxt, visited, stack)
    stack.append(now)


def _dfs(now, visited, stack):
    visited[now] = 1
    stack.append(now)
    for nxt in _graph[now]:
        if not visited[nxt]:
            _dfs(nxt, visited, stack)


stack = []
visited = [0] * (v+1)
# 모든 노드에서 정DFS
for i in range(1, v+1):
    if not visited[i]:
        dfs(i, visited, stack)

# 스택이 빌 때까지 pop 되는 요소에서 역DFS -> SCC 결과에 추가
visited = [0] * (v+1)
res = []
while stack:
    scc = []
    now = stack.pop()
    if not visited[now]:
        _dfs(now, visited, scc)
        res.append(sorted(scc))

print(len(res))
res = sorted(res)
for i in res:
    print(*i, end=' ')
    print(-1)