import sys
sys.stdin = open('../input.txt', 'r')
#####
# https://www.codetree.ai/training-field/frequent-problems/problems/cube-rounding-again/description?page=1&pageSize=20
# 1330 start 1430 end
from collections import deque


def rollD0():
    dice['u'], dice['b'], dice['d'], dice['f'] = dice['f'], dice['u'], dice['b'], dice['d']


def rollD1():
    dice['u'], dice['r'], dice['d'], dice['l'] = dice['l'], dice['u'], dice['r'], dice['d']


def rollD2():
    dice['f'], dice['u'], dice['b'], dice['d'] = dice['u'], dice['b'], dice['d'], dice['f']


def rollD3():
    dice['l'], dice['u'], dice['r'], dice['d'] = dice['u'], dice['r'], dice['d'], dice['l']


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상 우 하 좌
dice = {
    'u': 4,
    'd': 3,
    'f': 2,
    'b': 5,
    'r': 1,
    'l': 6
}
ans = 0
nd = 1
cx, cy = 0, 1
for _ in range(m):
    q = deque([[cx, cy]])
    visited = [[0]*n for _ in range(n)]
    visited[cx][cy] = 1
    base = arr[cx][cy]
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == base:
                q.append([nx, ny])
                visited[nx][ny] = 1

    ans += cnt * base

    # 다음 방향 설정
    if base < dice['d']:
        nd = (nd+1) % 4
    elif base > dice['d']:
        nd = (nd-1) % 4

    # 다음 위치 선정
    nx, ny = cx + dr[nd][0], cy + dr[nd][1]
    if 0 > nx or nx >= n or 0 > ny or ny >= n:
        nd = (nd+2) % 4
        nx, ny = cx + dr[nd][0], cy + dr[nd][1]

    cx, cy = nx, ny
    if nd == 0:
        rollD0()
    elif nd == 1:
        rollD1()
    elif nd == 2:
        rollD2()
    elif nd == 3:
        rollD3()
print(ans)