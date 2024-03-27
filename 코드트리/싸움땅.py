import sys
sys.stdin = open('../input.txt', 'r')
#####
# https://www.codetree.ai/training-field/frequent-problems/problems/battle-ground/description?page=1&pageSize=20
# 1600 시작 2000 End (1830 ~ 1950 특강 듣는다고 못품 : 2시간 40분 걸림..?)
# 정답 : 0 14 0 0 0 2 15 3 10 8
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def winneract(pid, r, c):
    x, y, d, s, g = people[pid]
    x, y = r, c
    ni, ng = -1, g
    for i in range(len(arr[x][y])):
        if ng < arr[x][y][i]:
            ni = i
            ng = arr[x][y][i]
    if g != ng:
        arr[x][y].pop(ni)
        arr[x][y].append(g)
    g = ng
    people[pid] = [x, y, d, s, g]


def loseract(pid, r, c):
    x, y, d, s, g = people[pid]
    x, y = r, c
    # 총 내려놓고
    if g > 0:
        arr[x][y].append(g)
        g = 0
    # 다음 진행 방향으로 한칸 전진
    for i in range(4):
        nx, ny = x + dx[(d+i) % 4], y + dy[(d+i) % 4]
        if 0 <= nx < n and 0 <= ny < n:
            flag = True
            # 다른 플레이어도 없어야함
            for other_pid in range(1, m+1):
                if pid == other_pid:
                    continue
                if [nx, ny] == [people[other_pid][0], people[other_pid][1]]:
                    flag = False
                    break
            if flag:
                d = (d+i) % 4
                x, y = nx, ny
                break
    if len(arr[x][y]):
        ni = -1
        ng = 0
        for i in range(len(arr[x][y])):
            if ng < arr[x][y][i]:
                ni = i
                ng = arr[x][y][i]
        # 지고난 후는 무조건 총이 없으니까 그냥 최대 총 할당
        if ni != -1:
            arr[x][y].pop(ni)
            g = ng
    people[pid] = [x, y, d, s, g]


def fight(pid, other_pid, r, c):
    power = people[pid][3] + people[pid][4]
    opower = people[other_pid][3] + people[other_pid][4]
    if power > opower:
        winner = pid
        loser = other_pid
    elif power < opower:
        winner = other_pid
        loser = pid
    else:
        if people[pid][3] > people[other_pid][3]:
            winner = pid
            loser = other_pid
        else:
            winner = other_pid
            loser = pid
    people[winner][0], people[winner][1] = r, c
    people[loser][0], people[loser][1] = r, c
    winp = people[winner][3] + people[winner][4]
    losp = people[loser][3] + people[loser][4]
    score[winner] += winp - losp
    loseract(loser, r, c)
    winneract(winner, r, c)


n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    lst = map(int, input().split())
    tmparr = []
    for i in lst:
        tmparr.append([i])
    arr.append(tmparr)

people = {}
for i in range(1, m+1):
    x, y, d, s = map(int, input().split()) # x, y, d, s
    people[i] = [x-1, y-1, d, s, 0] # 총 없음
score = [0] * (m+1)
for t in range(k):
    # print("##########  ", t, "  ########")

    # 1-1. 본인이 향하는 방향대로 한칸 이동
    for pid in people:
        x, y, d, s, g = people[pid]
        nx, ny = x+dx[d], y+dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            d = (d+2) % 4
            nx, ny = x+dx[d], y+dy[d]
        people[pid][2] = d
        x, y = nx, ny
        # 2-1-1. 플레이어가 있다면
        for other_pid in people:
            if other_pid == pid:
                continue
            # 겹치는 플레이어가 있으면
            if [x, y] == [people[other_pid][0], people[other_pid][1]]:
                # 싸우고 지지고 볶고
                fight(pid, other_pid, x, y)
                break
        # 2-1. 플레이어가 없다면
        else:
            # 총획득, 이때 해당 칸에 총 여러개일 수 있음
            # mg = max(arr[x][y])
            # if g < mg:
            #     g, mg = mg, g
            #     arr[x][y][arr.index(g)] = mg
            if len(arr[x][y]):
                mi = -1
                mg = -1
                for i in range(len(arr[x][y])):
                    if mg < arr[x][y][i]:
                        mi = i
                        mg = arr[x][y][i]
                if g == 0:
                    g = arr[x][y].pop(mi)
                else:
                    # g, arr[x][y][mi] = arr[x][y][mi], g
                    if mg > g:
                        arr[x][y].append(g)
                        g = arr[x][y].pop(mi)
            people[pid] = [x, y, d, s, g]
    #     print(pid, 'moved')
    #     print(people)
    #     for i in arr:
    #         print(i)
    #     print()
    # print("###END")
    # print(people)
    # print(score)
score.pop(0)
print(*score)