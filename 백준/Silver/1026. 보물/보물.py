
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sm = 0
for _ in range(n):
    sm += a.pop(a.index(min(a))) * b.pop(b.index(max(b)))
print(sm)