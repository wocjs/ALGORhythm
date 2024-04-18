
from collections import deque
import sys
input = sys.stdin.readline
dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
n, m = map(int, input().split())
arr = []
jq = deque()
fq = deque()
for i in range(n):
    tmp = list(input().strip())
    for j in range(m):
        if tmp[j] == 'J':
            jq.append([i, j])
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                print(1)
                exit(0)
    arr.append(tmp)
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'F':
            fq.append([i, j])
turn = 1
flag = False
while True:
    if flag:
        break
    njq = deque()
    while jq:
        x, y = jq.popleft()
        for dx, dy in dr:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '.':
                arr[nx][ny] = 'J'
                njq.append([nx, ny])

    nfq = deque()
    while fq:
        x, y = fq.popleft()
        for dx, dy in dr:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and (arr[nx][ny] == '.' or arr[nx][ny] == 'J'):
                arr[nx][ny] = 'F'
                nfq.append([nx, ny])
    # for i in arr:
    #     print(i)
    # print(njq)

    i = 0
    while i < len(njq):
        x, y = njq[i]
        if arr[x][y] != 'J':
            del njq[i]
            continue
        elif arr[x][y] == 'J' and (x == 0 or x == n-1 or y == 0 or y == m-1):
            flag = True
        i += 1
    # print(njq)
    if not njq:
        print('IMPOSSIBLE')
        exit(0)
    jq = njq
    fq = nfq
    turn += 1
print(turn)