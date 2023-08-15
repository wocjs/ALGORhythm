
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

house = []
chick = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i, j])
        elif arr[i][j] == 2:
            chick.append([i, j])

result = float('inf')
for c in combinations(chick, m):    # 각 치킨집들 선택한 것들에 대해
    dist = 0
    for h in house:     # 각각의 집마다
        tmp_d = float('inf')    # 한 집마다
        for select in range(m): # 선택한 치킨집 리스트들에 대해
            # 한 집마다 걸리는 치킨 거리를 선택한 치킨집과의 거리의 합의 최솟값(뭔소리고;)
            tmp_d = min(tmp_d, abs(h[0] - c[select][0]) + abs(h[1] - c[select][1]))
        dist += tmp_d
    result = min(result, dist)
print(result)