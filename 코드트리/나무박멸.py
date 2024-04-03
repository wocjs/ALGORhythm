import sys
sys.stdin = open('../input.txt', 'r')
#####
# 1315 start 1500 end
# https://www.codetree.ai/training-field/frequent-problems/problems/tree-kill-all/description?page=1&pageSize=20

n, m, k, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tdr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ddr = [[-1, -1], [1, 1], [-1, 1], [1, -1]]

dp = [[0] * n for _ in range(n)]
ans = 0
for years in range(m):
    # dp init
    for i in range(n):
        for j in range(n):
            if dp[i][j] > 0:
                dp[i][j] = 0
    trees = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                trees.append([i, j])
    # print("#################   ", years)
    # 1. 나무 성장
    for x, y in trees:
        cnt = 0
        for dx, dy in tdr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
                cnt += 1
        arr[x][y] += cnt
    # print('After step 1')
    # for i in arr:
    #     print(i)
    # 2. 번식
    for i in range(len(trees)):
        x, y = trees[i]
        chk = []
        for dx, dy in tdr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0 and dp[nx][ny] >= 0:
                chk.append([nx, ny])
        trees[i] = [x, y, chk]
    for x, y, chk in trees:
        if len(chk) == 0:
            continue
        spread = arr[x][y] // len(chk)
        for nx, ny in chk:
            arr[nx][ny] += spread
    # print('After step 2')
    # for i in arr:
    #     print(i)
    # print()
    # 3. 가장 많이 박멸되는 칸 찾기
    mx = 0
    mxidx = [10**9, 10**9]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                dp[i][j] = arr[i][j]
                for dx, dy in ddr:
                    for d in range(1, k+1):
                        nx, ny = i + dx*d, j + dy*d
                        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
                            dp[i][j] += arr[nx][ny]
                        else:
                            break
            if mx < dp[i][j]:
                mx = dp[i][j]
                mxidx = [i, j]
    ans += mx
    # print('find mx pos')
    # for i in dp:
    #     print(i)
    # print(mxidx)
    x, y = mxidx
    if [x, y] == [10**9, 10**9]:
        break
    dp[x][y] = -c-1
    arr[x][y] = 0
    for dx, dy in ddr:
        for d in range(1, k+1):
            nx, ny = x + dx*d, y + dy*d
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] >= 0:
                dp[nx][ny] = -c-1
                if arr[nx][ny] == 0:
                    break
                arr[nx][ny] = 0
            else:
                break
    for i in range(n):
        for j in range(n):
            if dp[i][j] < 0:
                dp[i][j] += 1
    # print('after spreads : dp')
    # for i in dp:
    #     print(i)
    # print('after spreads : arr')
    # for i in arr:
    #     print(i)
print(ans)
