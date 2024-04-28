
from collections import deque
n = int(input())
arr = list(i+1 for i in range(n))
arr = deque(arr)
while True:
    if len(arr) == 1:
        break
    arr.popleft()
    if len(arr) == 1:
        break
    arr.append(arr.popleft())
print(arr.pop())