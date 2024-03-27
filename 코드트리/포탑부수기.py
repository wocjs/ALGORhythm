import sys
sys.stdin = open('input.txt', 'r')
###### https://www.codetree.ai/problems/destroy-the-turret/description
# 1315 start 1823 end
from collections import deque


def select_attacker():
    def select_low_power():
        _coordinates = []
        power = float('inf')
        for i in range(n):
            for j in range(m):
                if arr[i][j]:
                    if power > arr[i][j]:
                        power = arr[i][j]
                        _coordinates = [[i, j]]
                    elif power == arr[i][j]:
                        _coordinates.append([i, j])
        return _coordinates

    def select_by_recent(_coordinates):
        res = [_coordinates[0]]
        d = attack_date[_coordinates[0][0]][_coordinates[0][1]]
        for i in range(1, len(_coordinates)):
            nd = attack_date[_coordinates[i][0]][_coordinates[i][1]]
            if d < nd:
                res = [_coordinates[i]]
                d = nd
            elif d == nd:
                res.append(_coordinates[i])
        return res

    def select_high_smRC(_coordinates):
        _coordinates = sorted(_coordinates, key=lambda x: -(x[0] + x[1]))  # 합이 큰거 우선
        res = [_coordinates[0]]
        sm = _coordinates[0][0] + _coordinates[0][1]
        # 정렬해도 같은거 있을 수 있으니 반복하며 비교
        for i in range(1, len(_coordinates)):
            nsm = _coordinates[i][0] + _coordinates[i][1]
            if sm < nsm:
                res = [_coordinates[i][0], _coordinates[i][1]]
                sm = nsm
            elif sm == nsm:
                res.append(_coordinates[i])
            else:
                break
        return res

    def select_high_row(_coordinates):
        _coordinates.sort(key=lambda x: -x[1])
        return _coordinates

    coordinates = select_low_power()
    if len(coordinates) == 1:
        return coordinates[0]

    coordinates = select_by_recent(coordinates)
    if len(coordinates) == 1:
        return coordinates[0]

    coordinates = select_high_smRC(coordinates)
    if len(coordinates) == 1:
        return coordinates[0]

    coordinates = select_high_row(coordinates)
    return coordinates[0]


def select_attackee(attacker):
    def select_high_power(attacker):
        _coordinates = []
        power = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] and [i, j] != attacker:
                    if power < arr[i][j]:
                        _coordinates = [[i, j]]
                        power = arr[i][j]
                    elif power == arr[i][j]:
                        _coordinates.append([i, j])
        return _coordinates

    def select_by_old(_coordinates):
        res = [_coordinates[0]]
        d = attack_date[_coordinates[0][0]][_coordinates[0][1]]
        for i in range(1, len(_coordinates)):
            nd = attack_date[_coordinates[i][0]][_coordinates[i][1]]
            if d > nd:
                res = [_coordinates[i]]
                d = nd
            elif d == nd:
                res.append(_coordinates[i])
        return res

    def select_low_sumRC(_coordinates):
        _coordinates.sort(key=lambda x: (x[0] + x[1]))
        res = [_coordinates[0]]
        sm = _coordinates[0][0] + _coordinates[0][1]
        for i in range(1, len(_coordinates)):
            nsm = _coordinates[i][0] + _coordinates[i][1]
            if sm > nsm:
                res = [_coordinates[i]]
                sm = nsm
            elif sm == nsm:
                res.append(_coordinates[i])
            else:
                break
        return res

    def select_low_row(_coordinates):
        _coordinates.sort(key=lambda x: x[1])
        return _coordinates

    coordinates = select_high_power(attacker)
    if len(coordinates) == 1:
        return coordinates[0]

    coordinates = select_by_old(coordinates)
    if len(coordinates) == 1:
        return coordinates[0]

    coordinates = select_low_sumRC(coordinates)
    if len(coordinates) == 1:
        return coordinates[0]

    coordinates = select_low_row(coordinates)
    return coordinates[0]


def chk_laser(sx, sy, ex, ey):
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if [x, y] == [ex, ey]:
            return True
        for dx, dy in dr:
            nx, ny = (x+dx) % n, (y+dy) % m
            if not visited[nx][ny] and arr[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])
                back[nx][ny] = [x, y]
    return False


def laser(sx, sy, ex, ey):
    # 일단 목표지점 공격
    arr[ex][ey] -= arr[sx][sy]
    attack_check[ex][ey] = 1
    if arr[ex][ey] < 0:
        arr[ex][ey] = 0
    q = [back[ex][ey]]
    while q[-1] != [sx, sy]:
        q.append(back[q[-1][0]][q[-1][1]])
    q.pop()
    for x, y in q:
        arr[x][y] -= arr[sx][sy] // 2
        attack_check[x][y] = 1
        if arr[x][y] < 0:
            arr[x][y] = 0


def bomb(sx, sy, ex, ey):
    power = arr[sx][sy]
    arr[ex][ey] -= power
    attack_check[ex][ey] = 1
    if arr[ex][ey] < 0:
        arr[ex][ey] = 0
    for dx, dy in aff_dr:
        nx, ny = (ex+dx) % n, (ey+dy) % m
        if [nx, ny] != [sx, sy]:
            arr[nx][ny] -= power // 2
            attack_check[nx][ny] = 1
            if arr[nx][ny] < 0:
                arr[nx][ny] = 0


def heal():
    for i in range(n):
        for j in range(m):
            if arr[i][j] and attack_check[i][j] == 0:
                arr[i][j] += 1


# 우 - 하 - 좌 - 상
dr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
aff_dr = [[-1, -1], [-1, 0], [-1, 1],
          [0, -1], [0, 1],
          [1, -1], [1, 0], [1, 1]]
n, m, k = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]
attack_date = [[0] * m for _ in range(n)]
for turn in range(1, k+1):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                cnt += 1
    if cnt <= 1:
        break
    attack_check = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    back = [[0]*m for _ in range(n)]

    attacker = select_attacker()
    arr[attacker[0]][attacker[1]] += n+m
    attackee = select_attackee(attacker)
    attack_date[attacker[0]][attacker[1]] = turn
    if chk_laser(attacker[0], attacker[1], attackee[0], attackee[1]):
        laser(attacker[0], attacker[1], attackee[0], attackee[1])
    else:
        bomb(attacker[0], attacker[1], attackee[0], attackee[1])
    attack_check[attacker[0]][attacker[1]] = 1
    heal()
    # if turn % 20 == 0:
    #     print(turn, attacker, attackee)
ans = 0
for i in arr:
    ans = max(ans, max(i))
print(ans)
