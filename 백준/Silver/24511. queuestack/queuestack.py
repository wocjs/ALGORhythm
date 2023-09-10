
import sys
intput = sys.stdin.readline
from collections import deque
n = int(input())
style = list(map(int, input().split()))
arr = list(map(int, input().split()))

m = int(input())
output = list(map(int, input().split()))

res_q = deque()

for i in range(n):
    if not style[i]:
        res_q.appendleft(arr[i])

# print(res_q)    # deque([4, 1])

for i in range(m):
    res_q.append(output[i])
    print(res_q.popleft(), end=' ')