
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m, c = map(int, input().split())
    f = c % n
    r = c//n + 1
    if f == 0:
        f = n
        r -= 1
    print(f, end='')
    if r < 10:
        r = '0' + str(r)
    print(r)