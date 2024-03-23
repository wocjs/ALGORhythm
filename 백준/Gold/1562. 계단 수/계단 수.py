
import sys
input = sys.stdin.readline

'''
0~9까지 10개의 수
1 << 10 == 2 ^ 10 == 1024
1024가 의미하는게 계단의 숫자를 사용했는지 안했는지에 대한 경우의 수
저장되는건 그 전의 자릿수가 +1이나 -1로 끝난 것의 합을 모두 더해주는 것
'''

mod = 1_000_000_000
n = int(input())
dp = [[0]*(1 << 10) for _ in range(10)]

# 시작자리 1로 설정
for i in range(1, 10):
    dp[i][1 << i] = 1

for i in range(1, n):
    dp_nxt = [[0]*1024 for _ in range(10)]
    # 0 ~ 9까지 순회
    for j in range(10):
        # 모든 비트에 대해 순회
        for k in range(1024):
            if j < 9:
                dp_nxt[j][k | (1<<j)] = (dp_nxt[j][k | (1<<j)] + dp[j+1][k]) % mod
            if j > 0:
                dp_nxt[j][k | (1<<j)] = (dp_nxt[j][k | (1<<j)] + dp[j-1][k]) % mod
    dp = dp_nxt
print(sum(dp[i][1023] for i in range(10)) % mod)