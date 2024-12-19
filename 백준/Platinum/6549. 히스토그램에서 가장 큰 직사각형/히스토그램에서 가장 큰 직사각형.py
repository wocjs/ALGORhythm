
import sys
input = sys.stdin.readline

res = []
while True:
    histogram = list(map(int, input().split()))
    if histogram[0] == 0:
        break
    stack = []
    n = histogram[0]
    max_area = 0
    for i in range(1, n+1):
        if len(stack) == 0:
            stack.append((i, histogram[i]))
        else:
            if stack[-1][1] <= histogram[i]:
                stack.append((i, histogram[i]))
            else:
                while len(stack) > 0 and stack[-1][1] > histogram[i]:
                    remove = stack.pop()
                    if len(stack) == 0:
                        width = i - 1
                    else:
                        width = i - stack[-1][0] - 1
                    max_area = max(max_area, remove[1] * width)
                stack.append((i, histogram[i]))
    while stack:
        remove = stack.pop()
        if len(stack) == 0:
            width = n
        else:
            width = (n - stack[-1][0])
        max_area = max(max_area, remove[1] * width)
    print(max_area)