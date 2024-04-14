import sys
sys.stdin = open('../input.txt', 'r')
###### https://www.codetree.ai/problems/destroy-the-turret/description
# 1947 start
from collections import deque


def sel_attacker():
    # find by low power
    lowpw = []
    power = float('inf')
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                if arr[i][j] < power:
                    lowpw = [[i, j]]
                    power = arr[i][j]
                elif arr[i][j] == power:
                    lowpw.append([i, j])
    if len(lowpw) == 1:
        return lowpw[0]
    # find by recent
    recent = []
    for x, y in lowpw:
        if not recent:
            recent.append([x, y])
            continue
        rx, ry = recent[-1]
        if att_date[x][y] > att_date[rx][ry]:
            recent = [[x, y]]
        elif att_date[x][y] == att_date[rx][ry]:
            recent.append([x, y])
    if len(recent) == 1:
        return recent[0]
    # find by sumrc
    rcsum = []
    for x, y in recent:
        if not rcsum:
            rcsum.append([x, y])
            continue
        sm = rcsum[0][0]+rcsum[0][1]
        s = x+y
        if s > sm:
            rcsum = [[x, y]]
        elif s == sm:
            rcsum.append([x, y])
    if len(rcsum) == 1:
        return rcsum[0]
    # find by col:
    column = []
    for x, y in rcsum:
        if not column:
            column.append([x, y])
            continue
        cc = column[-1][1]
        c = y
        if c > cc:
            column = [[x, y]]
    return column[0]


def sel_attackee(attacker):
    # find by strong power
    strpw = []
    power = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] and [i, j] != attacker:
                if power < arr[i][j]:
                    power = arr[i][j]
                    strpw = [[i, j]]
                elif arr[i][j] == power:
                    strpw.append([i, j])
    if len(strpw) == 1:
        return strpw[0]
    # find by old tower
    old = []
    for x, y in strpw:
        if not old:
            old.append([x, y])
            continue
        od = att_date[old[0][0]][old[0][1]]
        d = att_date[x][y]
        if d < od:
            old = [[x, y]]
        elif d == od:
            old.append([x, y])
    if len(old) == 1:
        return old[0]
    # find by rcsum
    rcsum = []
    for x, y in old:
        if not rcsum:
            rcsum.append([x, y])
            continue
        osm = rcsum[0][0] + rcsum[0][1]
        sm = x + y
        if sm < osm:
            rcsum = [[x, y]]
        elif sm == osm:
            rcsum.append([x, y])
    if len(rcsum) == 1:
        return rcsum[0]
    # find by least column
    column = []
    for x, y in rcsum:
        if not column:
            column.append([x, y])
            continue
        cc = column[0][1]
        c = y
        if c < cc:
            column = [[x, y]]
    return column[0]


def chkattackable(attacker, attackee):
    sx, sy = attacker
    ex, ey = attackee
    q = deque([[sx, sy]])
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if [x, y] == [ex, ey]:
            return True
        for dx, dy in dr:
            nx, ny = (x+dx) % n, (y+dy) % m
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = 1
                backchk[nx][ny] = [x, y]
    return False


def laser(attacker, attackee):
    sx, sy = attacker
    ex, ey = attackee
    # 일단 대상자 공격
    arr[ex][ey] -= arr[sx][sy]
    att_chk[ex][ey] = 1
    if arr[ex][ey] < 0:
        arr[ex][ey] = 0
    bq = [[ex, ey]]
    while bq[-1] != [sx, sy]:
        bq.append(backchk[bq[-1][0]][bq[-1][1]])
    pow = arr[sx][sy] // 2
    for i in range(1, len(bq)-1):
        arr[bq[i][0]][bq[i][1]] -= pow
        att_chk[bq[i][0]][bq[i][1]] = 1
        if arr[bq[i][0]][bq[i][1]] < 0:
            arr[bq[i][0]][bq[i][1]] = 0


def bomb(sx, sy, ex, ey):
    # 일단 공격
    arr[ex][ey] -= arr[sx][sy]
    att_chk[ex][ey] = 1
    if arr[ex][ey] < 0:
        arr[ex][ey] = 0
    pow = arr[sx][sy] // 2
    # 영향 받는 애들
    for dx, dy in adr:
        nx, ny = (ex+dx) % n, (ey+dy) % m
        if [sx, sy] != [nx, ny]:
            arr[nx][ny] -= pow
            att_chk[nx][ny] = 1
            if arr[nx][ny] < 0:
                arr[nx][ny] = 0


def chknotAttacked():
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not att_chk[i][j]:
                arr[i][j] += 1


dr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
adr = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
att_date = [[0]*m for _ in range(n)]

for turn in range(1, k+1):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                cnt += 1
    if cnt <= 1:
        break

    att_chk = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    backchk = [[0]*m for _ in range(n)]

    attacker = sel_attacker()
    arr[attacker[0]][attacker[1]] += n+m
    attackee = sel_attackee(attacker)
    # print(turn)
    # print(attacker, attackee)
    att_chk[attacker[0]][attacker[1]] = 1
    if chkattackable(attacker, attackee):
        laser(attacker, attackee)
        # print('laser')
    else:
        bomb(attacker[0], attacker[1], attackee[0], attackee[1])
        # print('bomb')
    chknotAttacked()
    att_date[attacker[0]][attacker[1]] = turn
    # for i in arr:
    #     print(i)
    # print()
power = 0
for i in range(n):
    power = max(power, max(arr[i]))
print(power)