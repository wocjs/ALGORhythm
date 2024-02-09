
# B1005
import sys
from collections import deque
T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    in_deg = [0] * (n+1)    # 진입차수
    time = [0] + list(map(int, input().split()))  # 시간
    graph = [[] for _ in range(n+1)]    # 진출노드
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_deg[b] += 1
    w = int(input())
    dp = [0] * (n+1)
    q = deque()
    for i in range(1, n+1):
        if in_deg[i] == 0:
            q.append(i)
            dp[i] = time[i]
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            in_deg[nxt] -= 1
            dp[nxt] = max(dp[now]+time[nxt], dp[nxt])
            if in_deg[nxt] == 0:
                q.append(nxt)
    print(dp[w])