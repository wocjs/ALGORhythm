dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1
    visited = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                visited[i][j] = 1
                q = [[i, j]]
                while q:
                    x, y = q.pop(0)
                    for dx, dy in dr:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            q.append([nx, ny])
                ans += 1
    print(ans)