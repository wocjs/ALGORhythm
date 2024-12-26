
import sys, math
input = sys.stdin.readline


def find_dist():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


def ignite(s):
    res = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            # 두 정점 사이에 간선이 없는 경우
            if not max_graph[i][j]:
                continue
            # 불이 i와 j에 전파되는 시간, a < b로 정렬
            a, b = sorted([dist[s][i], dist[s][j]])
            # b인 시점에 남아있는 간선의 길이
            remain = max_graph[i][j] - (b - a)
            res = max(res, b + remain / 2)
    return res


INF = float('inf')
n, m = map(int, input().split())
dist = [[0 if i == j else INF for j in range(n + 1)] for i in range(n + 1)]
# 태울 간선이 저장
max_graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    s, e, l = map(int, input().split())
    # dist에 가장 짧은 간선 저장
    dist[s][e] = min(dist[s][e], l)
    dist[e][s] = min(dist[e][s], l)
    # max_graph에 가장 긴 간선 저장
    max_graph[s][e] = max(max_graph[s][e], l)
    max_graph[e][s] = max(max_graph[e][s], l)

find_dist()
min_result = math.inf
for i in range(1, n + 1):
    min_result = min(min_result, ignite(i))
print(min_result)