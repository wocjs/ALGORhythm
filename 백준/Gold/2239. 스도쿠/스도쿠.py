# B2239
arr = [list(map(int, input().strip())) for _ in range(9)]
# 0의 위치를 튜플로 저장, dfs로 돌기전에 백트래킹으로 검사
zero = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero.append([i, j])
ln = len(zero)

# 행검사
def row_chk(r, num):
    for y in range(9):
        if num == arr[r][y]:
            return False
    return True

# 열검사
def col_chk(c, num):
    for x in range(9):
        if num == arr[x][c]:
            return False
    return True

# 박스 검사
def box_chk(r, c, num):
    _r = (r//3)*3
    _c = (c//3)*3
    for x in range(3):
        for y in range(3):
            if arr[_r+x][_c+y] == num:
                return False
    return True

def dfs(depth):
    if depth == len(zero):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end='')
            print()
        exit()
    r, c = zero[depth]
    for nm in range(1, 10):
        # dfs 돌기전에 검사해서 조건에 맞는거만 dfs 돔돔
        if row_chk(r, nm) and col_chk(c, nm) and box_chk(r, c, nm):
            arr[r][c] = nm
            dfs(depth+1)
            arr[r][c] = 0
            

dfs(0)
