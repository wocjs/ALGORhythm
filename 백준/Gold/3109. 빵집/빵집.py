import sys
sys.setrecursionlimit(int(1e8))

input = sys.stdin.readline

r, c = map(int, input().split())
maps = [list(map(str, input().rstrip())) for _ in range(r)]
count = 0
direction = [(-1, -1), (-1, 0), (-1, 1)]
def dfs(x, y):
    global count
    if x == 0:
        count += 1
        return True

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx and 0 <= ny and ny < r and maps[ny][nx] == '.':
            maps[ny][nx] = 'x'
            if dfs(nx, ny):   
                return True
    return False

for y in range(r):
    dfs(c - 1, y)

print(count)