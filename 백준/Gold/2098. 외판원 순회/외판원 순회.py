import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = {}
MX = float('inf')
def dfs(now, visited):
    # 1. 전체 방문했고, 출발위치(0)으로 돌아갈 수 있으면 리턴
    if visited == (1<<n)-1:
        if arr[now][0] != 0:
            return arr[now][0]
        else:
            return MX

    # 2. dp에 같은 값이 있으면(계산전적 있으면) 리턴
    if (now, visited) in dp:
        return dp[(now, visited)]

    min_cost = MX
    for nxt in range(1, n):
        # 갈 수 없거나 이미 방문한 곳이라면 건너뜀
        if arr[now][nxt] == 0 or visited & (1 << nxt):
            continue
        # 이제 여기서 DFS, 다익스트라 마냥 리턴받은값 갱신할것
        cost = dfs(nxt, visited | (1 << nxt)) + arr[now][nxt]
        min_cost = min(min_cost, cost)

    # dp에 now에서 다음 쭉 돌았을 때 값 저장
    dp[(now, visited)] = min_cost
    return min_cost


print(dfs(0, 1))
