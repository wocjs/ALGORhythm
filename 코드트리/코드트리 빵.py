# https://www.codetree.ai/problems/codetree-mon-bread/description
##### 1420 ~ 1705
import sys
from collections import deque
input = sys.stdin.readline

# 출발 후 경로 바뀌면 무빙도 달라져야함.


def caldist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)


# bfs
def cal_base_dist(sx, sy, ex, ey, dist):
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if visited[x][y] > dist:
            continue
        if [x, y] == [ex, ey]:
            return visited[x][y]-1
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and visitable[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])


def findNeaestBasecamp(sid):
    # bfs 안쓰고, basecamp중에서 하나씩 비교하면 될듯, 이때 거리는 BFS로 찾을 것
    dist = n**2 + 1
    x, y = 0, 0
    for bx, by in basecamps:
        bd = cal_base_dist(bx, by, store[sid][0], store[sid][1], dist)
        if bd and dist > bd:
            dist = bd
            x, y = bx, by
    return x, y, dist


# bfs 돌면서, 경로 기억해서 다음 경로 위치 제공
def findnxt(pid, px, py):
    sx, sy = store[pid]
    back = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append([px, py])
    visited[px][py] = 1
    while q:
        x, y = q.popleft()
        if [x, y] == [sx, sy]:
            break
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and visitable[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])
                back[nx][ny] = [x, y]
    res = [[sx, sy]]
    while True:
        x, y = res[-1]
        if [x, y] == [px, py]:
            res.pop()
            break
        res.append(back[x][y])
    x, y = res[-1]
    d = caldist(x, y, sx, sy)
    return x, y, d

dr = [[-1, 0], [0, -1], [0, 1], [1, 0]]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visitable = [[1]*n for _ in range(n)]
store = {}
cnt = 1
for _ in range(m):
    x, y = map(int, input().split())
    store[cnt] = [x-1, y-1]
    cnt += 1


basecamps = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            basecamps.append([i, j])

people = {}
t = 1
while True:
    # print('#############', t)

    # 1. 본인이 가고싶은 편의점 방향으로 1칸 움직임
    # 매번마다 갈 수 있는지 확인하고, 해당 경로로 이동해야함.
    for pid in range(1, m+1):
        if people.get(pid) is None:
            continue
        x, y, d = people[pid]
        x, y, d = findnxt(pid, x, y)
        people[pid] = [x, y, d]
        # for dx, dy in dr:
        #     nx, ny = x + dx, y + dy
        #     if 0 <= nx < n and 0 <= ny < n and visitable[nx][ny]:
        #         nd = caldist(nx, ny, store[pid][0], store[pid][1])
        #         if d > nd:
        #             people[pid] = [nx, ny, nd]
        #             break

    # 2. 편의점 도착하면 해당 편의점에서 멈춤, 이때부터 넌 못지나간다.
    for pid in range(1, m+1):
        if people.get(pid) is None:
            continue
        x, y, d = people[pid]
        if [x, y] == store[pid]:
            visitable[x][y] = 0
            del people[pid]

    # 3. 가까운 베이스캠프에 삽입(people 삽입) 행이 작은, 열이 작은 순으로
    dist = n**2
    for sid in range(1, m+1):
        if sid == t:
            x, y, d = findNeaestBasecamp(sid)
            people[sid] = [x, y, d]
            visitable[x][y] = 0
            basecamps.pop(basecamps.index([x, y]))

    if len(people) == 0:
        break
    t += 1
    # print(people)
    # for i in visitable:
    #     print(i)
print(t)

