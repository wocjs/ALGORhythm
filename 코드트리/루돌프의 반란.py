# import sys
# sys.stdin = open('input.txt', 'r')
##### https://www.codetree.ai/training-field/frequent-problems/problems/rudolph-rebellion/description?page=1&pageSize=20


def select_santa(deer_loc):
    r1, c1 = deer_loc
    close_dist = 2500
    select_santa_num = 0
    select_santa_loc = [0, 0]

    for i in santa:
        r2, c2 = santa[i]
        dist = (r1-r2)**2 + (c1-c2)**2
        if dist < close_dist:
            select_santa_num = i
            select_santa_loc = [r2, c2]
            close_dist = dist
        elif dist == close_dist:
            if r2 > select_santa_loc[0]:
                select_santa_num = i
                select_santa_loc = [r2, c2]
            elif r2 == select_santa_loc[0]:
                if c2 > select_santa_loc[1]:
                    select_santa_num = i
                    select_santa_loc = [r2, c2]
    return select_santa_num, select_santa_loc


def deer_move_rule(x1, y1, x2, y2):
    if x1 > x2:
        x1 -= 1
    elif x1 < x2:
        x1 += 1
    else:
        pass
    if y1 > y2:
        y1 -= 1
    elif y1 < y2:
        y1 += 1
    else:
        pass
    return x1, y1


def in_range(x, y):
    return 0 < x < N+1 and 0 < y < N+1


def check(p_num, x1, y1):
    for i in santa:
        if i == p_num:
            continue
        if santa[i] == [x1, y1]:
            return False, i
    return True, 0


def interaction(crush_new_santa_num, dir_x, dir_y):
    x, y = santa[crush_new_santa_num]
    nx, ny = x + dir_x, y + dir_y

    if not in_range(nx, ny):
        del santa[crush_new_santa_num]
        faint[crush_new_santa_num] = 0
    else:
        TF, p_num = check(crush_new_santa_num, nx, ny)
        if not TF:
            interaction(p_num, dir_x, dir_y)
        santa[crush_new_santa_num] = [nx, ny]


def deer_crash(deer_loc, x1, y1, p_num, x2, y2):
    santa_score[p_num] += C
    dir_x = x1 - deer_loc[0]   # 이동 위치 - 원래 위치
    dir_y = y1 - deer_loc[1]   # = 사슴 이동 방향

    x2 += dir_x*C
    y2 += dir_y*C

    if not in_range(x2, y2):
        del santa[p_num]
        faint[p_num] = 0
    else:   # 기절, 두 턴 뒤에 풀림
        faint[p_num] = 2
        # 날아간 자리에 산타 있는지 확인
        TF, crush_new_santa_num = check(p_num, x2, y2)
        if not TF:
            # 산타 있으면 상호작용
            interaction(crush_new_santa_num, dir_x, dir_y)
        santa[p_num] = [x2, y2]


def deer_move(deer_loc):
    x1, y1 = deer_loc
    p_num, [x2, y2] = select_santa(deer_loc)
    x1, y1 = deer_move_rule(x1, y1, x2, y2)

    # 충돌하면
    if [x1, y1] == [x2, y2]:
        # 원래 위치, 이동 위치[x1, y1], 목표 산타, 산타 위치 [x2, y2]
        deer_crash(deer_loc, x1, y1, p_num, x2, y2)
    return [x1, y1]


def santa_move_rule(p_num, x1, y1, deer_loc):
    x2, y2 = deer_loc
    dist = (x1-x2)**2 + (y1-y2)**2  # 현재 거리
    new_x, new_y = x1, y1
    for dx, dy in dr:
        nx, ny = x1 + dx, y1 + dy
        if in_range(nx, ny):
            ndist = (nx-x2)**2 + (ny-y2)**2
            if ndist < dist:
                TF, _ = check(p_num, nx, ny)
                if TF:
                    dist = ndist
                    new_x, new_y = nx, ny
    return new_x, new_y


def santa_crash(p_num, x1, y1):
    santa_score[p_num] += D
    dir_x = santa[p_num][0] - x1    # 원래 위치 - 이동 위치
    dir_y = santa[p_num][1] - y1    # = 산타 왔던 반대방향
    x1 += dir_x*D
    y1 += dir_y*D

    if not in_range(x1, y1):
        del santa[p_num]
        faint[p_num] = 0
    else:
        faint[p_num] = 2
        # 날아간 자리에 산타 있는지 확인
        TF, crush_new_santa_num = check(p_num, x1, y1)
        if not TF:
            # 산타 있으면 상호작용
            interaction(crush_new_santa_num, dir_x, dir_y)
        santa[p_num] = [x1, y1]



def santa_move(deer_loc):
    for i in range(1, P+1):
        if santa.get(i) == None:
            continue
        if faint[i] != 0:
            faint[i] -= 1
            continue

        x1, y1 = santa[i]
        x1, y1 = santa_move_rule(i, x1, y1, deer_loc)
        # 움직였는데 부딪칠 경우
        if [x1, y1] == deer_loc:
            santa_crash(i, x1, y1)
        else:
            santa[i] = [x1, y1]


dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# N:게임격자, M: 게임턴수, P:산타개수, C:루돌프 힘, D: 산타의 힘
N, M, P, C, D = map(int, input().split())
deer_loc = list(map(int, input().split()))
arr = [[0] * (N+1) for _ in range(N+1)]

santa = {}
for _ in range(P):
    sid, x, y = map(int, input().split())
    santa[sid] = [x, y]

# 기절상태 기록
faint = [0] * (P+1)
santa_score = [0] * (P+1)

# 게임 플레이 수 M
for k in range(1, M+1):
    # 루돌프 움직임
    deer_loc = deer_move(deer_loc)
    if len(santa) == 0:
        break

    # 1번 산타부터 P번 산타까지 움직임
    santa_move(deer_loc)
    if len(santa) == 0:
        break

    for pid in santa:
        santa_score[pid] += 1
print(*santa_score[1:])