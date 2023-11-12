n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 600
dr = [-1, 0, 1]

def dfs(row, col, d, fuel):
    global ans

    if row == n:
        ans = min(fuel, ans)
        return
    for dir in dr:
        if d != dir and 0 <= col + dir < m:
            dfs(row+1, col+dir, dir, fuel + arr[row][col])



for j in range(m):
    dfs(0, j, 2, 0)
print(ans)