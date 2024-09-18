
import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    data = deque(list(map(int, input().split())))

    res = 1
    while data:
        if data[0] < max(data):
            data.append(data.popleft())

        else:
            if m == 0:
                break
            data.popleft()
            res += 1
        m = m - 1 if m > 0 else len(data) - 1
    print(res)
