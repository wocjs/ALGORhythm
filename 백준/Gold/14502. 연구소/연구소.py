import copy
import sys
from collections import deque
input = sys.stdin.readline

def findSafezone():
    _arr = copy.deepcopy(arr)
    # 바이러스 출발점 찾기
    q = deque()
    for i in range(n):
        for j in range(m):
            if _arr[i][j] == 2:
                q.append([i, j])
    # 델타, bfs
    while q:
        x, y = q.popleft()
        for dr in range(4):
            nx = x + dx[dr]
            ny = y + dy[dr]
            if 0 <= nx < n and 0 <= ny < m and _arr[nx][ny] == 0:
                _arr[nx][ny] = 2
                q.append([nx, ny])
    # 0 찾기
    global ans
    cnt = 0
    for i in range(n):
        for j in range(m):
            if _arr[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)
def mkWall(cnt):
    if cnt == 3:
        findSafezone()
        return
    # 재귀 사용하여 벽을 3개 세울 수 있는 모든 경우의 수
    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                arr[i][j] = 1
                mkWall(cnt + 1)
                arr[i][j] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0
mkWall(0)
print(ans)