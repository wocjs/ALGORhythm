arr = [500, 100, 50, 10, 5, 1]
n = 1000 - int(input())
sm = 0
for c in arr:
    sm += n//c
    n = n%c
print(sm)