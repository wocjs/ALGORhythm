import sys
sys.stdin = open('../input.txt', 'r')
#####
# https://www.codetree.ai/training-field/frequent-problems/problems/odd-monopoly/description?page=2&pageSize=20
# 1400 start 1538 end
def move():
    for pid in range(1, m+1):
        if players.get(pid) is None:
            continue
        x, y, d = players[pid]
        for dx, dy in pdr[pid][d]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == []:
                nd = findr[(dx, dy)]
                players[pid] = [nx, ny, nd]
                break
        # 빈칸이 없으면 본인 독점계약칸으로 이동
        else:
            for dx, dy in pdr[pid][d]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny][0] == pid:
                    nd = findr[(dx, dy)]
                    players[pid] = [nx, ny, nd]
                    break
    # 중복 확인
    for i in range(1, m+1):
        if players.get(i) is None:
            continue
        for j in range(i+1, m+1):
            if players.get(j) is None:
                continue
            x, y = players[i][:2]
            ox, oy = players[j][:2]
            if [x, y] == [ox, oy]:
                del players[j]

    # 모든 칸 기간 -1
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                arr[i][j][1] -= 1
                if arr[i][j][1] == 0:
                    arr[i][j] = []

    # k초 적용
    for i in range(1, m+1):
        if players.get(i) is None:
            continue
        x, y = players[i][:2]
        arr[x][y] = [i, k]


dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
findr = {
    (-1, 0): 0,
    (1, 0): 1,
    (0, -1): 2,
    (0, 1): 3
}
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# player 초기화
players = {}
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            players[arr[i][j]] = [i, j]
            arr[i][j] = [arr[i][j], k]
        else:
            arr[i][j] = []
players = dict(sorted(players.items()))

lst = list(map(int, input().split()))
for i in range(1, m+1):
    players[i].append(lst[i-1]-1)

# 방향 초기화
pdr = {}
for pid in range(1, m+1):
    pdr[pid] = []
    for _ in range(4):
        d1, d2, d3, d4 = map(int, input().split())
        pdr[pid].append([dr[d1-1], dr[d2-1], dr[d3-1], dr[d4-1]])

# 움직이고, 1 뺀다음(이때 삭제도 같이) k적용
for t in range(1, 1001):
    move()
    if len(players) == 1:
        print(t)
        break
else:
    print(-1)