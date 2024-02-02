# B11779
import sys
import heapq
input = sys.stdin.readline

INF = 10 ** 9
n = int(input())
e = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
st, en = map(int, input().split())

dist = [INF] * (n + 1)
dist[st] = 0
prev = [0] * (n + 1)
q = [[0, st]]
while q:
    val, now = heapq.heappop(q)
    # pruning : 현재 처리중인 간선의 가중치 > 이제까지 발견된 경로
    if val > dist[now]:continue
    # 인접한 노드들 하나씩 확인
    for nVal, nxt in graph[now]:
        # 현재까지 가중치 + 다음까지 가는 가중치 < 다음에 저장된 가중치
        if dist[nxt] > val+nVal:
            dist[nxt] = val+nVal
            heapq.heappush(q, [dist[nxt], nxt])
            # 갱신이 되는 타이밍에 현재 -> 다음도 이음
            prev[nxt] = now

path = [en]
now = en
while now != st:
    now = prev[now]
    path.append(now)
print(dist[en])
print(len(path))
print(*path[::-1])