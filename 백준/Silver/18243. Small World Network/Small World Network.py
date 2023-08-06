v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
# for i in graph:
#     print(i)

def bfs(n):
    visited = [-1] * (v+1)
    q = [n]
    visited[n] = 0
    while q:
        node = q.pop(0)
        for n in graph[node]:
            if visited[n] == -1:
                q.append(n)
                visited[n] = visited[node] + 1
    for i in visited[1:n]:
        if i == -1 or 6 < i:
            return False
    return True

for i in range(1, v+1):
    ans = bfs(i)
    if not ans:
        print("Big World!")
        exit(0)
print("Small World!")