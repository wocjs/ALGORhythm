
# B1445
# 다익스트라 없이 일반 BFS로도 구현 가능했음
import heapq
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
mp = [[0]*m for _ in range(n)]
trash = []
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            st = [i, j]
        elif arr[i][j] == 'F':
            en = [i, j]
        elif arr[i][j] == 'g':
            trash.append([i, j])
            for dx ,dy in dr:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '.':
                    arr[nx][ny] = '#'

q = []
heapq.heappush(q, [0, 0, st[0], st[1]]) # cnt 2개, 시작점
visited = [[0]*m for _ in range(n)]
visited[st[0]][st[1]] = 1

while q:
    gcnt, ngcnt, x, y = heapq.heappop(q)
    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            if arr[nx][ny] == '.':
                heapq.heappush(q, [gcnt, ngcnt, nx, ny])
            elif arr[nx][ny] == '#':
                heapq.heappush(q, [gcnt, ngcnt+1, nx, ny])
            elif arr[nx][ny] == 'g':
                heapq.heappush(q, [gcnt+1, ngcnt, nx, ny])
            else:   # F 일 경우
                print(gcnt, ngcnt)
                break