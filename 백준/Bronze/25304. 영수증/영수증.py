
sm = int(input())
t = int(input())
_sm = 0
for _ in range(t):
    a, b = map(int, input().split())
    _sm += a*b
if _sm == sm:
    print('Yes')
else:
    print('No')