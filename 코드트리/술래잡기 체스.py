import sys
sys.stdin = open('../input.txt', 'r')
# https://www.codetree.ai/training-field/frequent-problems/problems/odd-chess2/description?page=2&pageSize=20
# 2010 start 2210 break 2230 resume 2300 end
from copy import deepcopy


def moveth(_tx, _ty, ar, _thief):
    _arr = deepcopy(ar)
    thief = deepcopy(_thief)
    for i in range(1, 17):
        if thief.get(i) is None:
            continue
        x, y, d = thief[i]
        dx, dy = dr[d]
        nx, ny = x + dx, y + dy
        while 0 > nx or nx >= 4 or 0 > ny or ny >= 4 or [_tx, _ty] == [nx, ny]:
            d = (d+1) % 8
            dx, dy = dr[d]
            nx, ny = x + dx, y + dy
        if _arr[nx][ny]:
            change_tid, change_tdr = _arr[nx][ny]
            thief[change_tid] = [x, y, change_tdr]
        # 딕셔너리 업데이트
        thief[i] = [nx, ny, d]
        # print('now moved i', i)
        _arr[x][y], _arr[nx][ny] = _arr[nx][ny], _arr[x][y]
        _arr[nx][ny] = [i, d]
        # print(x, y, nx, ny, d)
        # for __i in _arr:
        #     print(__i)
    return _arr, thief


def chkmovable(tx, ty, tdr, arrr, thief):
    global ans, res
    # 일단 움직이고
    # print('tx, ty : ', tx, ty, tdr)
    # print('before move')
    # for i in arrr:
    #     print(i)
    # print(thief)
    __arr, thief = moveth(tx, ty, arrr, thief)
    # 다음 도둑 잡으러감
    # print('after moved')
    # print(thief)
    # for i in __arr:
    #     print(i)
    for dist in range(1, 4):
        dx, dy = dr[tdr]
        nx, ny = tx + dx*dist, ty + dy*dist
        if 0 <= nx < 4 and 0 <= ny < 4 and __arr[nx][ny]:
            # 잡고 다음 이동
            copyidx, copydr = __arr[nx][ny]
            ans += copyidx
            thief[copyidx] = None
            # pr
            __arr[nx][ny] = []
            # print('Caught nxt')
            # for j in __arr:
            #     print(j)
            # print(nx, ny, __arr[nx][ny])
            chkmovable(nx, ny, copydr, __arr, thief)
            ans -= copyidx
            __arr[nx][ny] = [copyidx, copydr]
            thief[copyidx] = [nx, ny, copydr]
    else:
        # print(ans)
        # print()
        res = max(ans, res)
        return


#      0상     1좌상      2좌      3좌하     4하      5우하    6우     7우상
dr = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
arr = []
for _ in range(4):
    a, ar, b, br, c, cr, e, er = map(int, input().split())
    arr.append([[a, ar-1], [b, br-1], [c, cr-1], [e, er-1]])

ans = 0
res = 0
thief = {}
for i in range(4):
    for j in range(4):
        if i == 0 and j == 0:
            ans += arr[i][j][0]
            continue
        tid, td = arr[i][j]
        thief[tid] = [i, j, td]
thief = dict(sorted(thief.items()))
tx, ty = 0, 0
tdr = arr[0][0][1]
arr[0][0] = []

chkmovable(tx, ty, tdr, arr, thief)
print(res)