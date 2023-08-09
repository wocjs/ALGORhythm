
from collections import deque

N, K = map(int, input().split())       # N개의 줄에 걸쳐 나타나는 바이러스의 최대 크기는 K
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())     # S초 뒤 XY 좌표에 위치하는 바이러스

virus_lst = []                          # 현재 배열에서 존재하는 바이러스만 담을 리스트
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:                        # 주어진 배열을 돌며 바이러스만 골라 리스트에 담기
            virus_lst.append([arr[i][j], 0, i, j])  # 바이러스 크기, 시간, xy좌표

virus_lst.sort()                        # 바이러스 오름차순 정렬, 번호가 낮은 순으로 퍼지기 때문에 큐에도 먼저 넣어주기 위함

queue = deque(virus_lst)                # 큐에 바이러스 크기 리스트 넣기

while queue:
    virus, cnt, x, y = queue.popleft()
    if cnt == S:                        # 원하는 시간에 도달하면 중단
        break
    for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
        n_x, n_y = x+dx, y+dy
        if 0 <= n_x <= N-1 and 0 <= n_y <= N-1 and arr[n_x][n_y] == 0:  # 범위 안에 있고 아직 전파되지 않은 곳이라면
            arr[n_x][n_y] = virus                              # 바이러스 전파
            queue.append([virus, cnt+1, n_x, n_y])

print(arr[X-1][Y-1])