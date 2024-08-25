import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def makeTree(idx, st, en):
    # 기저조건
    if st == en:
        # leaf node set
        tree[idx] = [arr[st], arr[st]]
        return tree[idx]

    mid = (st+en) // 2
    l = makeTree(idx*2, st, mid)
    r = makeTree(idx*2+1, mid+1, en)

    # leaf노드 바로 위부터 mn, mx 세팅하면서 root까지 올라감
    tree[idx] = [min(l[0], r[0]), max(l[1], r[1])]  # 0번이 mn, 1번이 mx
    return tree[idx]


def find(idx, st, en):
    global r1, r2
    # 범위가 전혀 겹치지 않을 때
    if r2 < st or r1 > en:
        return [sys.maxsize, 0]  # 최대 min 값, 최소 max 값 반환

    # 범위가 트리 범위에 속할 때
    if r1 <= st and en <= r2:
        return tree[idx]

    mid = (st + en) // 2
    l = find(idx*2, st, mid)
    r = find(idx*2+1, mid+1, en)
    return [min(l[0], r[0]), max(l[1], r[1])]


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
# tree size = 2^(log2(n)+1) : 대충 귀납법으로 봤을 때 이 사이즈해도 가능
tree = [0] * (2**math.ceil(math.log2(n)+1))
_ = makeTree(1, 0, len(arr)-1)

for _ in range(m):
    r1, r2 = map(int, input().split())
    r1 -= 1
    r2 -= 1
    ans = find(1, 0, len(arr) - 1)
    print(*ans)