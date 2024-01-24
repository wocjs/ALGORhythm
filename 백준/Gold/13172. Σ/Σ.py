# B13172
import sys
input  = sys.stdin.readline
sys.setrecursionlimit(10**9)
def mul(b, t):
    if t == 1:
        return b % X
    if t % 2 == 0:
        tmp = mul(b, t//2)  # 여기서 logN으로 준다!
        return (tmp*tmp) % X
    else:
        return b*mul(b, t-1) % X    # 이건 1에 수렴이라 신경 ㄴㄴ

X = 1000000007
m = int(input())
sm = 0

for _ in range(m):
    b, a = map(int, input().split())
    sm += a*mul(b, X-2) % X
print(sm % X)
