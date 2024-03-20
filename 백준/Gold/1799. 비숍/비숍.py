
# B1799
import copy


def except_by_color(arr, color):  # 특정 색을 제외시켜주는 함수
    for i in range(n):
        for j in range(n):
            if color == "white":
                if (i+j) % 2 == 0:
                    arr[i][j] = 0
            if color == "black":
                if (i+j) % 2 != 0:
                    arr[i][j] = 0



def find(idx, arr):
    global lq
    global ans
    # 종료조건 : 끝까지 놓아 보았을 때
    if idx == lq:
        # 끝까지 돌아봤으니 max값 갱신
        tmp = 0
        for i in range(n):
            tmp += sum(arr[i])
        ans = max(tmp, ans)
        return

    # 놓을 수 있는지 판단
    x, y = q[idx]
    flag = True
    # 영향을 받을 자리들 0인지 체크
    for dx, dy in dr:
        for i in range(1, n):
            nx = x + dx * i
            ny = y + dy * i
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny]:
                    flag = False
                    break
        if flag is False:
            break

    # 놓을 수 있으면 놓아보고 다음 인덱스 진행
    if flag:
        arr[x][y] = 1
        find(idx+1, arr)
        arr[x][y] = 0
    # 못놓았다면, 못 놓은채로 다음 인덱스 진행
    find(idx+1, arr)


n = int(input())
Arr = [list(map(int, input().split())) for _ in range(n)]
dr = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
# 흑/백으로 나눠서 절반씩 두번 계산하는게 더 빠름
white_board = copy.deepcopy(Arr)
black_board = copy.deepcopy(Arr)
except_by_color(white_board, "black")
except_by_color(black_board, "white")

answer = 0

q = []
for i in range(n):
    for j in range(n):
        if white_board[i][j]:
            q.append([i, j])
            white_board[i][j] = 0
lq = len(q)
ans = 0
find(0, white_board)
answer += ans

q = []
for i in range(n):
    for j in range(n):
        if black_board[i][j]:
            q.append([i, j])
            black_board[i][j] = 0
lq = len(q)
ans = 0
find(0, black_board)
print(answer + ans)