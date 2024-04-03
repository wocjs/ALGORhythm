import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = list(input().strip() for _ in range(n))

dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

rx, ry, bx, by = 10, 10, 10, 10
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j

q = deque()
q.append([rx, ry, bx, by])
visited = set()
visited.add((rx, ry, bx, by))
cnt = 0
while q:
    # 여기 반복문이 신의 한수임.
    # 현재 가볼 수 있는 곳 다 탐색해보고 한번 추가하는거니까
    # generation 느낌..?
    for _ in range(len(q)):
        rx, ry, bx, by = q.popleft()
        if cnt > 10:
            print(-1)
            exit()
        if arr[rx][ry] == 'O':
            print(cnt)
            exit()
        for dx, dy in dr:
            nrx, nry = rx + dx, ry + dy
            while True:
                if arr[nrx][nry] == "#":
                    nrx, nry = nrx - dx, nry - dy
                    break
                elif arr[nrx][nry] == 'O':
                    break
                nrx, nry = nrx + dx, nry + dy

            nbx, nby = bx + dx, by + dy
            while True:
                if arr[nbx][nby] == "#":
                    nbx, nby = nbx - dx, nby - dy
                    break
                elif arr[nbx][nby] == 'O':
                    break
                nbx, nby = nbx + dx, nby + dy

            # 파랑이 구멍위치이면
            if arr[nbx][nby] == 'O':
                continue
            # 빨강, 파랑 위치 같으면 더 많이 움직인 놈 한칸 뒤로
            if [nrx, nry] == [nbx, nby]:
                if abs(nrx-rx) + abs(nry-ry) < abs(nbx-bx) + abs(nby-by):
                    nbx, nby = nbx - dx, nby - dy
                else:
                    nrx, nry = nrx - dx, nry - dy

            if (nrx, nry, nbx, nby) not in visited:
                q.append([nrx, nry, nbx, nby])
                visited.add((nrx, nry, nbx, nby))
    cnt += 1
print(-1)
