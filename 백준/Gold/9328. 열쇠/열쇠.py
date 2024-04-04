
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = [list(input().strip()) for _ in range(n)]
    sk_key = list(input().strip())

    visited = [[0]*m for _ in range(n)]
    if sk_key[0] == '0':
        sk_key = []
    q = deque()
    Q = deque()
    ans = 0

    # 입장 가능한 곳 찾기 가로
    for j in range(1, m-1):
        if arr[0][j] == '.':
            q.append([0, j])
            visited[0][j] = 1
        elif arr[0][j] == '$':
            ans += 1
            q.append([0, j])
            visited[0][j] = 1
        elif arr[0][j].islower():
            sk_key.append(arr[0][j])
            q.append([0, j])
            visited[0][j] = 1

        if arr[n-1][j] == '.':
            q.append([n-1, j])
            visited[n-1][j] = 1
        elif arr[n-1][j] == '$':
            ans += 1
            q.append([n-1, j])
            visited[n-1][j] = 1
        elif arr[n-1][j].islower():
            sk_key.append(arr[n-1][j])
            q.append([n-1, j])
            visited[n-1][j] = 1
    # 입장 가능한 곳 찾기 세로
    for i in range(n):
        if arr[i][0] == '.':
            q.append([i, 0])
            visited[i][0] = 1
        elif arr[i][0] == '$':
            ans += 1
            q.append([i, 0])
            visited[i][0] = 1
        elif arr[i][0].islower():
            sk_key.append(arr[i][0])
            q.append([i, 0])
            visited[i][0] = 1

        if arr[i][m-1] == '.':
            q.append([i, m-1])
            visited[i][m-1] = 1
        elif arr[i][m-1] == '$':
            ans += 1
            q.append([i, m-1])
            visited[i][m-1] = 1
        elif arr[i][m-1].islower():
            sk_key.append(arr[i][m-1])
            q.append([i, m-1])
            visited[i][m-1] = 1
    # 대문자
    for j in range(m):
        if arr[0][j].isupper():
            if arr[0][j].lower() in sk_key:
                q.append([0, j])
                visited[0][j] = 1
            else:
                Q.append([0, j])
        if arr[n-1][j].isupper():
            if arr[n-1][j].lower() in sk_key:
                q.append([n-1, j])
                visited[n-1][j] = 1
            else:
                Q.append([n-1, j])
    for i in range(n):
        if arr[i][0].isupper():
            if arr[i][0].lower() in sk_key:
                q.append([i, 0])
                visited[i][0] = 1
            else:
                Q.append([i, 0])
        if arr[i][m-1].isupper():
            if arr[i][m-1].lower() in sk_key:
                q.append([i, m-1])
                visited[i][m-1] = 1
            else:
                Q.append([i, m-1])
    # print(sk_key, q, Q)
    while True:
        while q:
            x, y = q.popleft()
            for dx, dy in dr:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if arr[nx][ny] == '.':
                        q.append([nx, ny])
                        visited[nx][ny] = 1
                    elif arr[nx][ny] == '$':
                        visited[nx][ny] = 1
                        q.append([nx, ny])
                        ans += 1
                    elif arr[nx][ny].islower():
                        sk_key.append(arr[nx][ny])
                        q.append([nx, ny])
                        visited[nx][ny] = 1
                    elif arr[nx][ny].isupper():
                        if arr[nx][ny].lower() in sk_key:
                            q.append([nx, ny])
                            visited[nx][ny] = 1
                        else:
                            Q.append([nx, ny])
        i = 0
        preQ = deepcopy(Q)
        while True:
            if i >= len(Q):
                break
            x, y = Q[i]
            if arr[x][y].lower() in sk_key:
                q.append([x, y])
                visited[x][y] = 1
                del Q[i]
                continue
            i += 1
        if preQ == Q:
            break
    print(ans)
