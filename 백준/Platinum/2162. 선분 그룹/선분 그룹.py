import sys
input = sys.stdin.readline
# 문제 참조 https://www.acmicpc.net/problem/17387
# 이론 참조 https://velog.io/@frog_slayer/Algo-CCW%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%84%A0%EB%B6%84%EA%B5%90%EC%B0%A8%ED%8C%90%EC%A0%95
# 해설 참조 https://rccode.tistory.com/199
'''
선분교차판정 + unionFind
'''
# 여기서


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)


def chk(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    mx1, my1 = min(x1, x2), min(y1, y2)
    mx2, my2 = max(x1, x2), max(y1, y2)
    mx3, my3 = min(x3, x4), min(y3, y4)
    mx4, my4 = max(x3, x4), max(y3, y4)

    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    # parallel
    if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return True
    # cross
    elif ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
        return True

    return False
# 여기까진 좀 외웁시다


def find(x):
    if par[x] != x:
        par[x] = find(par[x])
    return par[x]


def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        par[y] = x
    else:
        par[x] = y


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

par = [i for i in range(n)]

for i in range(n - 1):
    for j in range(i+1, n):
        # 선분이 교차할 시 두 그룹 합침
        if chk(arr[i], arr[j]):
            union(i, j)

# par를 통해 출력값을 얻음
gcnt = 0
lines = [0] * n
for i in range(n):
    # 자기 자신을 가리키면 루트 노드
    if i == par[i]:
        gcnt += 1
    lines[find(i)] += 1

print(gcnt)
print(max(lines))
