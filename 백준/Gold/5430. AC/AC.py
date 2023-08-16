
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    msg = input()
    l = int(input())
    _arr = input()
    arr = deque()
    tmp = ''
    for char in _arr:
        if char.isdecimal():
            tmp += char
        elif char == "," or char == "]":
            arr.append(tmp)
            tmp = ''

    rev, front, back = 0, 0, len(arr)-1

    if l == 0:
        arr = []
        front = 0
        back = 0

    flag = True
    for m in msg:
        if m == 'R':
            rev += 1
        elif m == 'D':
            if len(arr) == 0:
                flag = False
                break
            else:
                if not rev % 2:
                    arr.popleft()
                else:
                    arr.pop()
    if flag:
        if rev % 2:
            arr.reverse()
            print("[" + ','.join(arr) + ']')
        else:
            print("[" + ','.join(arr) + ']')
    else:
        print('error')