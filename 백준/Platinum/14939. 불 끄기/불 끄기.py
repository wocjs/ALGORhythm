
import sys
input = sys.stdin.readline
from copy import deepcopy
'''
브루트포스와 그리디를 활용하여 비트마스킹으로 접근
첫 행은 전구 10개에 대해 키고 끄는 모든 경우의 수(2^10 = 1024)에 대해 모두 확인
두번째 행 부터는 윗 행의 전구가 켜져 있는 경우에만 스위치를 누르는 방식
'''
dr = [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]]
res = 101
arr = [[0]*10 for _ in range(10)]
for i in range(10):
    tmp = input()
    for j in range(10):
        if tmp[j] == 'O':
            arr[i][j] = 1

# 첫 줄 모든 경우의 수
for bit in range(1 << 10):
    new_arr = deepcopy(arr)
    cnt = 0
    # 첫 줄 10개 전구 하나씩 탐색
    for k in range(10):
        if bit & (1 << k):
            cnt += 1
            # 맨 위 방향 체크
            for dx, dy in dr:
                nx, ny = 0+dx, k+dy
                if 0 <= nx < 10 and 0 <= ny < 10:
                    new_arr[nx][ny] = not new_arr[nx][ny]

    for i in range(1, 10):
        for j in range(10):
            if new_arr[i-1][j]:
                cnt += 1
                for dx, dy in dr:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < 10 and 0 <= ny < 10:
                        new_arr[nx][ny] = not new_arr[nx][ny]
    if sum(new_arr[-1]) == 0:
        res = min(res, cnt)
print(res) if res < 101 else print(-1)
