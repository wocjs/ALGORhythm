
# B17386
# CCW 알고리즘
# a X b = (a2b3-a3b2, a3b1-a1b3, a1b2-a2b1)
import sys
input = sys.stdin.readline


def ccw(a1, b1, a2, b2, a3, b3):
    res = a1*b2 + a2*b3 + a3*b1 - a2*b1 - a3*b2 - a1*b3
    if res > 0:
        return -1
    elif res < 0:
        return 1
    else:
        return 0


def find():
    # parallel
    if c123*c124 == 0 and c341*c342 == 0:
        _x1, _y1, _x2, _y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        _x3, _y3, _x4, _y4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)
        if _x1 <= _x4 and _x3 <= _x2 and _y1 <= _y4 and _y3 <= _y2:
            return 1
    # cross:
    elif c123*c124 <= 0 and c341*c342 <= 0:
        return 1
    return 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

c123 = ccw(x1, y1, x2, y2, x3, y3)
c124 = ccw(x1, y1, x2, y2, x4, y4)
c341 = ccw(x3, y3, x4, y4, x1, y1)
c342 = ccw(x3, y3, x4, y4, x2, y2)

print(find())
