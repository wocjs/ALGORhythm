
import sys
input = sys.stdin.readline
n = int(input())
stack = {}
for _ in range(n):
    name, log = map(str, input().split())
    if log == 'enter':
        stack[name] = 1
    else:
        stack[name] = 0
lst = sorted(stack, reverse=True)
for nm in lst:
    if stack[nm]:
        print(nm)