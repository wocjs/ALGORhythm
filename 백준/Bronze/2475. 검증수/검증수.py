arr = list(map(int, input().split()))
sm = 0
for i in arr:
    sm += i**2
print(sm % 10)