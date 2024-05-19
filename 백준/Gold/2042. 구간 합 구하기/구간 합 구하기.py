
import sys
input = sys.stdin.readline

# init tree
def init(st, en, idx):
    # st와 en이 같으면 리프노드
    if st == en:
        tree[idx] = lst[st]
        return tree[idx]
    # 현재 노드는 왼쪽 아래 노드와 오른쪽 아래 노드의 합
    mid = (st + en) // 2
    tree[idx] = init(st, mid, idx*2) + init(mid+1, en, idx*2 + 1)
    return tree[idx]


# 현재 노드 x
def update(x, left, right, idx, val):
    # 길이 1인 구간
    if left == right and right == idx:
        tree[x] = val
        return
    # 현재 구간에 idx 포함 X
    if idx < left or right < idx:
        return

    # 이분탐색
    mid = (left++right) // 2
    update(x*2, left, mid, idx, val)
    update(x*2+1, mid+1, right, idx, val)
    # 업데이트된 자식 노드들을 통해 현재 노드 업데이트
    tree[x] = tree[x*2]+tree[x*2 + 1]


def find(b, c, x, left, right):
    # b~c 구간이 현재 트리 구간에 포함 X
    if c < left or right < b:
        return 0
    # b~c 안에 현재 트리 포함
    if b <= left and right <= c:
        return tree[x]
    # 구간이 겹치는 경우
    mid = (left+right) // 2
    return find(b, c, x*2, left, mid) + find(b, c, x*2+1, mid+1, right)


n, m, k = map(int, input().split())

lst = []
tree = [0]*(n*4)    # 1차원 lst로 표현할 트리 == seg_tree

for _ in range(n):
    lst.append(int(input()))

init(0, n-1, 1)
# print(tree)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    # update : b -> c
    if a == 1:
        update(1, 0, n-1, b-1, c)
    else:
        sm = find(b-1, c-1, 1, 0, n-1)
        print(sm)