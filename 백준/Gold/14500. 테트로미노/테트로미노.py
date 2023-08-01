
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(x, y, c, t):
    if c == 4:
        global ans
        ans = max(t, ans)
        return
    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, c+1, t+arr[nx][ny])
            visited[nx][ny] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        cnt = 0
        dfs(i, j, cnt, 0)

# ㅏ
for i in range(n-2):
    for j in range(m-1):
        ans = max(ans, arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j+1])
# ㅓ
for i in range(n-2):
    for j in range(1, m):
        ans = max(ans, arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j-1])
# ㅗ
for i in range(1, n):
    for j in range(m-2):
        ans = max(ans, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i-1][j+1])
#ㅜ
for i in range(n-1):
    for j in range(m-2):
        ans = max(ans, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1])
print(ans)
