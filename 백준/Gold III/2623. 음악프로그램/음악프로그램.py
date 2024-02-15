# B2623
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_deg = [0]*(n+1)

for _ in range(m):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)-1):
        graph[arr[i]].append(arr[i+1])
        in_deg[arr[i+1]] += 1

q = []
for i in range(1, n+1):
    if in_deg[i] == 0:
        q.append(i)
ans = []
while q:
    now = q.pop(0)
    ans.append(now)
    for nxt in graph[now]:
        in_deg[nxt] -= 1
        if in_deg[nxt] == 0:
            q.append(nxt)
if sum(in_deg) != 0:
    print(0)
else:
    for i in ans:
        print(i)