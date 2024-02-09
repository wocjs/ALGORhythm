
# B17404
import sys
input = sys.stdin.readline

INF = float('inf')
R, G, B = 0, 1, 2

n = int(input())
arr = [[-1, -1, -1]]

for _ in range(n):
    arr.append(list(map(int, input().split())))

ans = INF
# dp를 3번 해야함
for color in [R, G, B]:
    dp = [[-1, -1, -1] for _ in range(n+1)]
    dp[1] = [INF, INF, INF]
    # 시작 색깔을 돌아가며 설정함
    dp[1][color] = arr[1][color]
    # dp 일단끝까지 감
    for i in range(2, n+1):
        dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + arr[i][R]
        dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + arr[i][G]
        dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + arr[i][B]
    # 시작이랑 같은 인덱스의 dp위치에 INF로 갱신
    dp[n][color] = INF
    # 최솟값 구하고, 이걸 전체 color번 반복함
    ans = min(ans, min(dp[n]))
print(ans)