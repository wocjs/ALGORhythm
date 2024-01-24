
def ans(n, s):
    return s*mul(n, X-2)%X

def mul(b, t):
    if t == 1:
        return b%X
    if t%2 == 0:
        tmp = mul(b, t//2)
        return (tmp*tmp)%X
    else:
        return b*mul(b, t-1)%X

X = 1000000007
m = int(input())
sm = 0

for _ in range(m):
    a, b = map(int, input().split())
    sm += ans(a, b) % X
print(sm%X)
