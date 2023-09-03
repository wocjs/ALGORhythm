import sys
sys.setrecursionlimit(100000)

def dfs(idx):
    global res
    visited[idx] = 1
    team.append(idx)
    num = arr[idx]

    if visited[num]:
        if num in team:
            res += team[team.index(num):]
        return
    else:
        dfs(num)



T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    res = []

    for i in range(1, n + 1):
        if not visited[i]:
            team = []
            dfs(i)
    print(n-len(res))