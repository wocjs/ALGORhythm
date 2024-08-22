
import sys
input = sys.stdin.readline
n = int(input())
sm1, sm2 = 100, 100
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        sm2 -= a
    elif a < b:
        sm1 -= b
print(sm1)
print(sm2)