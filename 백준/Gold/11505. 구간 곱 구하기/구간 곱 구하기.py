
import sys
import math
input = sys.stdin.readline
X = 1_000_000_007


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
    else:
        mid = (start+end) // 2
        tree[index] = init(start, mid, 2*index) * init(mid + 1, end, 2*index + 1) % X
    return tree[index]


def find(start, end, index, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[index]

    mid = (start+end) // 2
    return find(start, mid, 2*index, left, right) * find(mid+1, end, 2*index + 1, left, right) % X


def update(start, end, index, where, diff):
    if where < start or end < where:
        return

    if start == end:
        tree[index] = diff
    else:
        mid = (start + end) // 2
        update(start, mid, index * 2, where, diff)
        update(mid + 1, end, index * 2 + 1, where, diff)
        tree[index] = tree[2 * index] * tree[2 * index + 1] % X


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * (2**(int(math.ceil(math.log2(N))) + 1))
init(0, N-1, 1)
for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1:  # 수 변경
        update(0, N-1, 1, b-1, c)

    else:       # 구간 곱 구하기
        print(find(0, N-1, 1, b-1, c-1))
