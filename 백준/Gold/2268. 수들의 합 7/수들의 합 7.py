
import sys
import math
input = sys.stdin.readline
n, m = map(int, input().split())
tree = [0] * 2**(math.ceil(math.log2(n)) + 1)

def interval_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]

    return interval_sum(node * 2, start, (start + end) // 2, left, right) \
        + interval_sum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

def update(node, start, end, idx, val):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = val
        return

    update(node * 2, start, (start + end) // 2, idx, val)
    update(node * 2 + 1, (start + end) // 2 + 1, end, idx, val)

    tree[node] = tree[node*2] + tree[node*2+1]

for i in range(m):
    q, a, b = map(int, input().split())

    if q == 0:
        if a > b:
            a, b = b, a
        print(interval_sum(1, 0, n-1, a-1, b-1))
    else:
        update(1, 0, n-1, a-1, b)