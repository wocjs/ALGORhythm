
# B11758
# CCW 알고리즘
# a X b = (a2b3-a3b2, a3b1-a1b3, a1b2-a2b1)
import sys
p1 = list(map(int, sys.stdin.readline().split()))
p2 = list(map(int, sys.stdin.readline().split()))
p3 = list(map(int, sys.stdin.readline().split()))
v1 = [p2[0]-p1[0], p2[1]-p1[1], 0]  # p12
v2 = [p3[0]-p2[0], p3[1]-p2[1], 0]  # p23
# 2차원이기 때문에 z값은 0.
# 따라서 외적값의 i, j, k 방뱡 중 i, j 방향 벡터값은 0임.
# 시계 : 음수, 직선 : 0, 반시계 : 양수
res = (v1[0]*v2[1] - v1[1]*v2[0])
if res > 0:
    print(1)
elif res < 0:
    print(-1)
else:
    print(0)
