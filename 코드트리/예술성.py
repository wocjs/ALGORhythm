import sys
sys.stdin = open('../input.txt', 'r')
#####
# https://www.codetree.ai/training-field/frequent-problems/problems/artistry/description?page=1&pageSize=20
# 1346 시작 1415 휴식 1445 휴식끝 1515 끝
import sys
input = sys.stdin.readline
from collections import deque


def getsm():
    global ans
    visited = [[0] * n for _ in range(n)]
    group = {}
    q = deque()
    cnt = 1
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q.append([i, j])
                visited[i][j] = 1
                group[cnt] = [[i, j]]
                while q:
                    x, y = q.popleft()
                    for dx, dy in dr:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[x][y] == arr[nx][ny]:
                            visited[nx][ny] = 1
                            q.append([nx, ny])
                            group[cnt].append([nx, ny])
                cnt += 1
    k = len(group)
    for gid in range(1, k + 1):
        gl1 = len(group[gid])
        for oth_gid in range(gid + 1, k + 1):
            gl2 = len(group[oth_gid])
            side = 0
            for x1, y1 in group[gid]:
                for x2, y2 in group[oth_gid]:
                    if abs(x2 - x1) + abs(y2 - y1) == 1:
                        side += 1
            ans += (gl1 + gl2) * arr[x1][y1] * arr[x2][y2] * side


def rotate():
    # 십자모양 회전
    x, y = n // 2, n // 2
    for i in range(1, n // 2 + 1):
        arr[x][y - i], arr[x - i][y], arr[x][y + i], arr[x + i][y] = arr[x - i][y], arr[x][y + i], arr[x + i][y], \
        arr[x][
            y - i]

    # 나머지 4개 정사각형 회전
    for sx, sy in [[0, 0], [0, n // 2 + 1], [n // 2 + 1, 0], [n // 2 + 1, n // 2 + 1]]:
        tmp = [[0] * (n // 2) for _ in range(n // 2)]
        for i in range(n // 2):
            for j in range(n // 2):
                tmp[i][j] = arr[sx + i][sy + j]

        tmp = list(zip(*tmp[::-1]))
        for i in range(n // 2):
            for j in range(n // 2):
                arr[sx + i][sy + j] = tmp[i][j]


dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

getsm()
for _ in range(3):
    rotate()
    getsm()
print(ans)