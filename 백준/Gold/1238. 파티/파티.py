
# B1238
import heapq
INF = float('inf')

def find(st):
    dist = [INF] * (n+1)
    dist[st] = 0
    q = []
    heapq.heappush(q, [0, st])
    while q:
        val, now = heapq.heappop(q)
        if dist[now] >= val:    # pruning
            for nxtVal, nxt in arr[now]:
                # 현재 값 + 다음 노드로 가는데 드는 값이 다음 노드에 저장된 값보다 작으면
                if val + nxtVal < dist[nxt]:
                    dist[nxt] = val + nxtVal
                    heapq.heappush(q, [val+nxtVal, nxt])

    return dist


n, m, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    arr[a].append([t, b])

ans = find(x)
for i in range(1, n+1):
    if i != x:
        tmp = find(i)
        ans[i] += tmp[x]
print(max(ans[1:]))