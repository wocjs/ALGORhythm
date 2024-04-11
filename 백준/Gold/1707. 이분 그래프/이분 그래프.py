from collections import deque
import sys
input = sys.stdin.readline


def bfs(node, group):
    q = deque([node])
    visited[node] = group
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = visited[now] * -1
            elif visited[nxt] == visited[now]:
                return False
    return True


t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    graph = [[]for _ in range(v+1)]
    visited = [0]*(v+1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 탐색 시작
    for i in range(1, v+1):
        if not visited[i]:
            res = bfs(i, 1)
            if not res:
                break

    print("YES") if res else print("NO")