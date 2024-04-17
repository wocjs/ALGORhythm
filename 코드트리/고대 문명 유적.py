import sys
sys.stdin = open('../input.txt', 'r')
#####
def findsm(_arr):
    visited = [[0]*n for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                tmp = []
                q = deque([[i, j]])
                tmp.append([i, j])
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    for dx, dy in dr:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and _arr[x][y] == _arr[nx][ny] and not visited[nx][ny]:
                            tmp.append([nx, ny])
                            q.append([nx, ny])
                            visited[nx][ny] = 1
                if len(tmp) >= 3:
                    for x in tmp:
                        res.append(x)
    if len(res) >= 3:
        return True, res
    else:
        return False, res


def rotate():
    res = []
    for i in range(3):
        for j in range(3):
            tmp = [[0]*3 for _ in range(3)]
            for r in range(3):
                for c in range(3):
                    tmp[r][c] = arr[i+r][j+c]
            # 90도 회전
            tmp = list(zip(*tmp[::-1]))
            for r in range(3):
                for c in range(3):
                    arr[i+r][j+c] = tmp[r][c]
            TF, _res = findsm(arr)
            if TF:
                res.append([_res, 1, i, j])
            # 180도 회전
            tmp = list(zip(*tmp[::-1]))
            for r in range(3):
                for c in range(3):
                    arr[i+r][j+c] = tmp[r][c]
            TF, _res = findsm(arr)
            if TF:
                res.append([_res, 2, i, j])
            # 270도 회전
            tmp = list(zip(*tmp[::-1]))
            for r in range(3):
                for c in range(3):
                    arr[i + r][j + c] = tmp[r][c]
            TF, _res = findsm(arr)
            if TF:
                res.append([_res, 3, i, j])
            # 360도 회전
            tmp = list(zip(*tmp[::-1]))
            for r in range(3):
                for c in range(3):
                    arr[i + r][j + c] = tmp[r][c]
    res.sort(key=lambda x:(-len(x[0]), x[1], x[3], x[2]))
    if res:
        return True, res[0]
    else:
        return False, []


dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
from collections import deque
k, m = map(int, input().split())
n = 5
arr = [list(map(int, input().split())) for _ in range(n)]
lst = deque(list(map(int, input().split())))
ans = []
for turn in range(k):
    TF, _lst = rotate()
    if not TF:
        break
    res, rcnt, r, c = _lst
    tmp = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            tmp[i][j] = arr[r+i][c+j]
    for _ in range(rcnt):
        tmp = list(zip(*tmp[::-1]))
    for i in range(3):
        for j in range(3):
            arr[r+i][c+j] = tmp[i][j]
    ans.append(0)
    ans[turn] += len(res)
    res.sort(key=lambda x:(x[1], -x[0]))
    for x, y in res:
        arr[x][y] = lst.popleft()
    while True:
        TF, res = findsm(arr)
        if not TF:
            break
        ans[turn] += len(res)
        res.sort(key=lambda x: (x[1], -x[0]))
        for x, y in res:
            arr[x][y] = lst.popleft()

print(*ans)