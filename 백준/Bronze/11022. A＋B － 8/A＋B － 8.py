
import sys
input = sys.stdin.readline
for tc in range(1, int(input())+1):
    a, b = map(int, input().split())
    print(f'Case #{tc}: {a} + {b} = {a+b}')