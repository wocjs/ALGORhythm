
import sys
input = sys.stdin.readline
oasis = [int(input()) for _ in range(int(input()))]

stack = []
res = 0
for o in oasis:
  while stack and stack[-1][0]<o:
    res += stack.pop()[1]
  if not stack:
    stack.append((o, 1))
    continue
  if stack[-1][0]==o:
    cnt = stack.pop()[1]
    res += cnt
    if stack: res += 1
    stack.append((o, cnt+1))
  else:
    stack.append((o, 1))
    res += 1
print(res)
