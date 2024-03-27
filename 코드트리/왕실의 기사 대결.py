##### https://www.codetree.ai/training-field/frequent-problems/problems/royal-knight-duel/description?page=1&pageSize=20
# 1430 start, 1920 end
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def chkmovable(idx, direction):
    global L
    r, c, h, w, k = knightlst[idx]
    for x in range(r, r+h):
        for y in range(c, c+w):
            nx = x + dx[direction]
            ny = y + dy[direction]
            # L 넘어가거나, 벽에 밀린다면 return False
            if nx < 0 or L <= nx or ny < 0 or L <= ny or arr[nx][ny] == 2:
                return False
            # 다른 기사가 있다면 먼저 밀릴 수 있는 지 확인
            if loc[nx][ny] != 0 and loc[nx][ny] != idx and loc[nx][ny] not in pushed:
                # 재귀 호출할 때 기사의 번호를 사용
                if not chkmovable(loc[nx][ny], direction):
                    return False
                pushed.append(loc[nx][ny])
    return True


def move_knight(idx, direction):
    # 움직이기 - 기존의 위치에서 한칸씩 땡겨야 함.
    if chkmovable(idx, direction):
        pushed.append(idx)
        for i in pushed:
            r, c, h, w, k = knightlst[i]
            q = []
            for x in range(r, r + h):
                for y in range(c, c + w):
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    loc[x][y] = 0
                    q.append([nx, ny])
            while q:
                nx, ny = q.pop()
                loc[nx][ny] = i
            knightlst[i] = [r + dx[direction], c + dy[direction], h, w, k]
        return True


# 입력
L, N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(L)]
loc = [[0] * L for _ in range(L)]
knightlst = {}
for i in range(1, N+1):
    r, c, h, w, k = map(int, input().split())
    knightlst[i] = [r-1, c-1, h, w, k]
    for _i in range(h):
        for _j in range(w):
            loc[r-1+_i][c-1+_j] = i
orderlst = [list(map(int, input().split())) for _ in range(Q)]
ans = [0]*(N+1)


# for i in loc:
#     print(i)
# 명령 받고
for idx, direction in orderlst:
    if knightlst.get(idx) is None:  # 없는 기사면 pass
        continue
    pushed = []
    # 움직이면
    # print(knightlst)
    # print("order : ", idx, direction)
    if move_knight(idx, direction):
        # print("#### Success ####")
        # print("Pushed : ", pushed)
        # for i in loc:
        #     print(i)
        for i in range(1, N+1):
            if idx == i:
                continue
            if knightlst.get(i) is None:
                continue
            if i not in pushed:
                continue

            r, c, h, w, k = knightlst[i]
            for _i in range(r, r+h):
                for _j in range(c, c+w):
                    if arr[_i][_j] == 1:
                        k -= 1
                        ans[i] += 1
            if k <= 0:
                del knightlst[i]
                for __i in range(r, r+h):
                    for __j in range(c, c+w):
                        loc[__i][__j] = 0
                ans[i] = 0
            else:
                knightlst[i] = [r, c, h, w, k]
    # else:
    #     print("#### Fail ####")
    #     print("Pushed : ", pushed)
    #     for i in loc:
    #         print(i)
    # print("ans : ", ans)
print(sum(ans))
