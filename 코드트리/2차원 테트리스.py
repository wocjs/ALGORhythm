import sys
sys.stdin = open('../input.txt', 'r')
#####
# https://www.codetree.ai/training-field/frequent-problems/problems/tetris-2d/description?page=2&pageSize=20
# 1435 시작 1600 end 1트 합격 짝짝
from copy import deepcopy
n = int(input())

dr = {
    'y': [1, 0],
    'r': [0, 1]
}
tpe = {
    1: [[0, 0]],
    2: [[0, 0], [0, 1]],
    3: [[0, 0], [1, 0]]
}
arr = [[0]*10 for _ in range(10)]
tCnt = 0


def movable(_chklst, color):
    for x, y in _chklst:
        dx, dy = dr[color]
        nx, ny = x + dx, y + dy
        if 0 > nx or nx >= 10 or 0 > ny or ny >= 10 or arr[nx][ny] == 1:
            return False
    return True


def move(_chklst, color):
    res = []
    for x, y in _chklst:
        dx, dy = dr[color]
        res.append([x + dx, y + dy])
    return res


def tetris(idx, color):
    # 빨강 이면 열삭제
    if color == 'r':
        for y in range(idx, 3, -1):
            for x in range(4):
                arr[x][y] = arr[x][y-1]
    # 노랑 이면 행삭제
    elif color == 'y':
        for x in range(idx, 3, -1):
            for y in range(4):
                arr[x][y] = arr[x-1][y]
    else:
        print('error')


for _ in range(n):
    # print("######## ", _)
    t, r, c = map(int, input().split())
    chklst = []
    for x, y in tpe[t]:
        chklst.append([r+x, c+y])
    # 빨강 움직임
    redchklst = deepcopy(chklst)
    while movable(redchklst, 'r'):
        redchklst = move(redchklst, 'r')
    for x, y in redchklst:
        arr[x][y] = 1
    # 노랑 움직임
    yelchklst = deepcopy(chklst)
    while movable(yelchklst, 'y'):
        yelchklst = move(yelchklst, 'y')
    for x, y in yelchklst:
        arr[x][y] = 1
    # print('Now chklst : ', chklst)
    # print('After Moved')
    # for i in arr:
    #     print(i)
    # print()
    # 빨강 테트리스 확인
    for j in range(6, 10):
        sm = 0
        for i in range(4):
            sm += arr[i][j]
        if sm == 4:
            tCnt += 1
            tetris(j, 'r')
    # 노랑 테트리스 확인
    for i in range(6, 10):
        sm = 0
        for j in range(4):
            sm += arr[i][j]
        if sm == 4:
            tCnt += 1
            tetris(i, 'y')
    # print('After red, yel tetris')
    # for i in arr:
    #     print(i)
    # 빨강 연한부분 확인
    while True:
        sm = 0
        for i in range(4):
            sm += arr[i][5]
        if sm == 0:
            break
        else:
            tetris(9, 'r')
    # 노랑 연한부분 확인
    while True:
        sm = 0
        for j in range(4):
            sm += arr[5][j]
        if sm == 0:
            break
        else:
            tetris(9, 'y')
print(tCnt)
left = 0
for i in range(10):
    for j in range(10):
        if arr[i][j]:
            left += 1
print(left)