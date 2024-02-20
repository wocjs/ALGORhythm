
# B11049
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
'''
ABCDE연속행렬 곱의 최솟값 =
min(ABCDE,
min(A) + min(BCDE) + 합치는 비용(A행 * A열 * E열),
min(AB) + min(CDE) + 합치는 비용(A행 * B열 * E열),
min(ABC) + min(DE) + 합치는 비용(A행 * C열 * E열),
min(ABCD) + min(E) + 합치는 비용(A행 * D열 * E열)
)
'''
# print(arr)
for i in range(1, n):
    for j in range(n-i):
        if i == 1:
            dp[j][j+i] = arr[j][0] * arr[j][1] * arr[j+i][1]
        dp[j][j+i] = float('inf')
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i],
                             dp[j][k] + dp[k+1][j+i] +
                             arr[j][0] * arr[k][1] * arr[j+i][1]
                             )

# for i in dp:
#     print(i)
print(dp[0][n-1])