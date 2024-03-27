import sys
sys.stdin = open('input.txt', 'r')
##### https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner/description?page=1&pageSize=20
# 1300 시작 1718 끝
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def calcdist(x, y):
    return abs(ext[0] - x) + abs(ext[1] - y)


def mov():
    global movsm
    for pid in range(1, m+1):
        if people.get(pid) is None:
            continue
        x, y, d = people[pid]
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                nd = calcdist(nx, ny)
                if nd < d and arr[nx][ny] == 0:
                    people[pid] = [nx, ny, nd]
                    movsm += 1
                    if [nx, ny] == ext:
                        del people[pid]
                    break


def find_box():
    # print(pid)
    ex, ey = ext
    for size in range(2, n+1):  # 2 ~ 10포함
        for i in range(n-size+1):   # 10-size+1
            for j in range(n-size+1):
                for pid in range(1, m+1):
                    if people.get(pid) is None:
                        continue
                    px, py, pd = people[pid]
                    if i <= px < i+size and j <= py < j+size and i <= ex < i+size and j <= ey < j+size:
                        return [size, i, j]


def rotate():
    global ext
    # # 참가자 선택
    # selected_pid = 0
    # person = [0, 0, n ** 2]
    # for pid in range(1, m+1):
    #     if people.get(pid) is None:
    #         continue
    #     # 거리 짧은 순 갱신
    #     if people[pid][2] < person[2]:
    #         person = people[pid]
    #         selected_pid = pid
    #     # 거리 같다면
    #     elif people[pid][2] == person[2]:
    #         # r 작은것 우선
    #         if people[pid][0] < person[0]:
    #             person = people[pid]
    #             selected_pid = pid
    #         # r 같다면
    #         elif people[pid][0] == person[0]:
    #             # c 작은것 우선
    #             if people[pid][1] < person[1]:
    #                 person = people[pid]
    #                 selected_pid = pid
    ############
    # 행렬 사이즈, 위치 선정
    size, x, y = find_box()
    # print(size, x, y)
    tmparr = [[0] * size for _ in range(size)]
    #복사
    for i in range(size):
        for j in range(size):
            tmparr[i][j] = arr[x+i][y+j]

    # 출구 중복 회전 방지 + 참가자 중복 회전 방지용 플래그
    chk = [0]*(m+1)
    # 행렬 회전 [i][j] -> [x+j][y+size-i-1]
    for i in range(size):
        for j in range(size):
            arr[x+j][y+size-i-1] = tmparr[i][j]
            # 회전이 중복으로 발생함
            for pid in range(1, m+1):
                if people.get(pid) is None:
                    continue
                px, py, pd = people[pid]
                # 참가자 있으면 업데이트
                if [px, py] == [x+i, y+j] and not chk[pid]:
                    px, py = x+j, y+size-i-1
                    people[pid] = [px, py, pd]
                    chk[pid] = 1
            # 출구 포함되어있으면 업데이트
            if [x+i, y+j] == ext and not chk[0]:
                ext = [x+j, y+size-i-1]
                chk[0] = 1
            if arr[x+j][y+size-i-1] > 0:
                arr[x+j][y+size-i-1] -= 1
    for pid in range(1, m+1):
        if people.get(pid) is None:
            continue
        x, y, d = people[pid]
        people[pid] = [x, y, calcdist(x, y)]


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
people = {}

for i in range(1, m + 1):
    _x, _y = map(int, input().split())
    people[i] = [_x - 1, _y - 1]
_x, _y = list(map(int, input().split()))
ext = [_x - 1, _y - 1]
for i in range(1, m + 1):
    people[i].append(calcdist(people[i][0], people[i][1]))

movsm = 0
for _ in range(k):
    # print("exit : ", ext)
    # print("#########", _)
    # print('before move')
    # print(people)
    mov()
    # print('after move')
    # print(people)
    if len(people) == 0:
        break
    # print('before rotate')
    # for i in arr:
    #     print(i)
    # print()
    rotate()
    # print('after rotate')
    # print(people)
    # print('rotated map')
    # for i in arr:
    #     print(i)
    # print("exit : ", ext)

print(movsm)
print(ext[0]+1, ext[1]+1)
