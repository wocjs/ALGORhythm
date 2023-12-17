arr = [list(map(int, input().split())) for _ in range(4)]
for i in arr:
    x1, y1, p1, q1, x2, y2, p2, q2 = i
    # case (d)
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')
    elif x1 == p2 or x2 == p1:
    # case (c)
        if q1 == y2 or q2 == y1:
            print('c')
    # case (b)
        else:
            print('b')
    elif q1 == y2 or q2 == y1:
        print('b')
    # case (a)
    else:
        print('a')