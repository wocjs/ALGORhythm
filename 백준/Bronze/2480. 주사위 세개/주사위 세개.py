
a, b, c = map(int, input().split())
sm = 0
if a == b and b == c:
    sm = 10000 + a*1000
elif a == b:
    sm = 1000 + a*100
elif b == c:
    sm = 1000 + b*100
elif c == a:
    sm = 1000 + c*100
else:
    sm = max(a, b, c) * 100
print(sm)