n, m, k = map(int, input().split())
arr = [[0] * (m) for _ in range(n)]
# for i in arr:
#     print(i)
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1
            # print(i, j)

dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = []
for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            q = [[i, j]]
            cnt = 1
            while q:
                x, y = q.pop(0)
                arr[x][y] = 1
                for dx, dy in dr:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
                        arr[nx][ny] = 1
                        q.append([nx, ny])
                        cnt += 1
            ans.append(cnt)
ans.sort()
print(len(ans))
print(*ans)