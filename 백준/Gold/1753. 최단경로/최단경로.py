
import sys
import heapq
input = sys.stdin.readline

INF = float('inf')
V, E = map(int, input().split())
K = int(input())
arr = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
# print(arr)
table = [INF] * (V + 1)

def dijkstra():
    table[K] = 0
    q = []
    heapq.heappush(q, [0, K])
    # print(table)
    while q:
        nowVal, now = heapq.heappop(q)
        # print(now, nowVal)
        if nowVal > table[now]:
            # print('Prunning')
            continue
        for i in arr[now]:
            if table[i[0]] > (nowVal + i[1]):
                table[i[0]] = nowVal + i[1]
                heapq.heappush(q, [nowVal + i[1], i[0]])
            # print(table)
        # print(q)
    for i in range(1, V + 1):
        if table[i] == INF:
            print('INF')
        else:
            print(table[i])


dijkstra()