
# B 1865
import sys
input = sys.stdin.readline
INF = 10**9

# 전체 노드를 시작점으로 할 필요 없음
# 사이클이 있는지만 보면 되어서 아무 곳에서 시작 가능
def find(st):
    dist = [INF] * (n+1)
    dist[st] = 0
    for _i in range(n):
        # 매 반복마다 모든 간선 확인
        for now, nxt, cost in arr:
            # 현재 노드에 도달이 가능하면서,
            # 다음 노드로 이동하는 거리가 갱신 가능하면
            # if dist[now] != INF and dist[nxt] > cost + dist[now]:
            if dist[nxt] > cost + dist[now]:
                dist[nxt] = cost + dist[now]
                if _i == n-1:
                    return True
    return False

T = int(input())
for tc in range(T):
    n, m, w = map(int, input().split())
    arr = []

    # road
    for _ in range(m):
        s, e, t = map(int, input().split())
        arr.append([s, e, t])
        arr.append([e, s, t])
    # wormhole
    for _ in range(w):
        s, e, t = map(int, input().split())
        arr.append([s, e, -t])

    # Find with every start node
    if find(1):
        print('YES')
    else:
        print("NO")