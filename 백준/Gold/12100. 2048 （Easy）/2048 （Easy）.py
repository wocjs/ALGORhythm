# B12100
import sys
import copy
input = sys.stdin.readline


def left(_arr):
    for i in range(n):
        idx = 0  # 수동 조작 인덱스
        for j in range(1, n):
            if _arr[i][j] != 0:  # 0이 아닌 값이 있으면
                tmp = _arr[i][j]
                _arr[i][j] = 0
                # 수동 조작 인덱스 자리에 넣을거임
                if _arr[i][idx] == 0:  # 비어 있으면 그대로 옮김
                    _arr[i][idx] = tmp
                elif _arr[i][idx] == tmp:  # 같은 값이면 두배로
                    _arr[i][idx] = tmp * 2
                    idx += 1
                else:   # 비어 있지 않고 다른 값이면
                    idx += 1    # pass
                    _arr[i][idx] = tmp
    return _arr


def right(_arr):
    for i in range(n):
        idx = n-1
        for j in range(n-1, -1, -1):
            if _arr[i][j] != 0:
                tmp = _arr[i][j]
                _arr[i][j] = 0
                if _arr[i][idx] == 0:
                    _arr[i][idx] = tmp
                elif _arr[i][idx] == tmp:
                    _arr[i][idx] = tmp * 2
                    idx -= 1
                else:
                    idx -= 1
                    _arr[i][idx] = tmp
    return _arr


def up(_arr):
    for j in range(n):
        idx = 0
        for i in range(n):
            if _arr[i][j] != 0:
                tmp = _arr[i][j]
                _arr[i][j] = 0
                if _arr[idx][j] == 0:
                    _arr[idx][j] = tmp
                elif _arr[idx][j] == tmp:
                    _arr[idx][j] = tmp * 2
                    idx += 1
                else:
                    idx += 1
                    _arr[idx][j] = tmp
    return _arr


def down(_arr):
    for j in range(n):
        idx = n-1
        for i in range(n-1, -1, -1):
            if _arr[i][j] != 0:
                tmp = _arr[i][j]
                _arr[i][j] = 0
                if _arr[idx][j] == 0:
                    _arr[idx][j] = tmp
                elif _arr[idx][j] == tmp:
                    _arr[idx][j] = tmp * 2
                    idx -= 1
                else:
                    idx -= 1
                    _arr[idx][j] = tmp
    return _arr


def dfs(c, Arr):
    global ans
    if c == 5:
        for i in range(n):
            ans = max(ans, max(Arr[i]))
        return
    _Arr = copy.deepcopy(Arr)
    dfs(c + 1, left(_Arr))

    _Arr = copy.deepcopy(Arr)
    dfs(c + 1, right(_Arr))

    _Arr = copy.deepcopy(Arr)
    dfs(c + 1, up(_Arr))

    _Arr = copy.deepcopy(Arr)
    dfs(c + 1, down(_Arr))


n = int(input())
ARR = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(0, ARR)
print(ans)
