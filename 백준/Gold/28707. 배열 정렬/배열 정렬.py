import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
A = ''
lst = list(map(int, input().split()))
for i in lst:
    A += str(i-1)
m = int(input())
q = [list(map(int, input().split())) for _ in range(m)]
pq = [(0, A)]
dist = {A: 0}

# dijkstra
while pq:
    cost, now = heappop(pq)
    # prunning
    if dist[now] < cost:
        continue

    for l, r, c in q:
        # 조작 결과
        nxt = now[:l-1] + now[r-1] + now[l:r-1] + now[l-1] + now[r:]
        if nxt not in dist or dist[nxt] > cost+c:
            dist[nxt] = cost + c
            heappush(pq, (cost+c, nxt))

A = ''.join(sorted(A))
if A not in dist:
    print(-1)
else:
    print(dist[A])