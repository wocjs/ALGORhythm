
import sys
input = sys.stdin.readline


def check(x1, y1, x2, y2, x3, y3, x4, y4):
    if ccw(x1, y1, x3, y3, x4, y4) * ccw(x2, y2, x3, y3, x4, y4) == 0:
        if ccw(x3, y3, x1, y1, x2, y2) * ccw(x4, y4, x1, y1, x2, y2) == 0:
            if (x1, y1) > (x2, y2):
                x1, x2 = x2, x1;
                y1, y2 = y2, y1
            if (x3, y3) > (x4, y4):
                x3, x4 = x4, x3;
                y3, y4 = y4, y3
            if (x2, y2) >= (x3, y3) and (x1, y1) <= (x4, y4):
                return True
            else:
                return False

    if ccw(x1, y1, x3, y3, x4, y4) * ccw(x2, y2, x3, y3, x4, y4) <= 0:
        if ccw(x3, y3, x1, y1, x2, y2) * ccw(x4, y4, x1, y1, x2, y2) <= 0:
            return True
    return False


def ccw(a1, b1, a2, b2, a3, b3):
    result = (a1 * b2 + a2 * b3 + a3 * b1) - (a1 * b3 + a3 * b2 + a2 * b1)
    return result


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

if check(x1, y1, x2, y2, x3, y3, x4, y4):
    print(1)
    try:
        x = ((x1*y2-y1*x2)*(x3-x4) - (x3*y4-x4*y3)*(x1-x2)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
        y = ((x1*y2-y1*x2)*(y3-y4) - (x3*y4-y3*x4)*(y1-y2)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
        print(x, y)
    except:
        if (x1, y1) > (x2, y2):
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if (x3, y3) > (x4, y4):
            x3, x4 = x4, x3
            y3, y4 = y4, y3
        if x2 == x3 and y2 == y3:
            print(x2, y2)
        elif x1 == x4 and y1 == y4:
            print(x1, y1)
else:
    print(0)