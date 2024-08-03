import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(st):
    global c
    global visited
    visited[st] = 1
    # leaf node에서 [0, 1]
    if len(c[st]) == 0:
        dp[st][0] = 0
        dp[st][1] = 1
    else:
        for i in c[st]:
            if visited[i] == 0:
                dfs(i)
                # 현재 얼리어답터면 자식은 상관없고 최소 얼리어딥터 수 구함
                dp[st][1] += min(dp[i])
                # 현재 얼리어답터가 아니면 node의 자식들은 모두 얼리 어답터
                dp[st][0] += dp[i][1]
        # 현재 얼리어답터인경우 1 추가
        dp[st][1] += 1


n = int(input())
c = [[] for _ in range(n+1)]
# dp[현재노드][얼리 어답터 여부]
dp = [[0, 0] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    c[a].append(b)
    c[b].append(a)

visited = [0] * (n+1)

dfs(1)
print(min(dp[1]))