
import sys
input = sys.stdin.readline


def update(t, diff, idx, s, e):
    if e < t or t < s:
        return

    tree[idx] += diff
    if s != e:
        update(t, diff, idx * 2, s, (s + e) // 2)
        update(t, diff, idx * 2 + 1, (s + e) // 2 + 1, e)


def find(count, idx, start, end):
    if start == end:  # 리프노드 도달
        return start

    else:
        if tree[idx * 2] >= count:
            return find(count, idx * 2, start, (start + end) // 2)
        else:
            return find(count - tree[idx * 2], idx * 2 + 1, (start + end) // 2 + 1, end)


N = 1000000  # 맛 종류
nums = [0] * (N + 1)
tree = [0] * (2 ** 21)

M = int(input())
for _ in range(M):
    order, *cont = map(int, input().split())
    if order == 2:
        update(cont[0], cont[1], 1, 1, N)
        nums[cont[0]] += cont[1]

    else:
        eat = find(cont[0], 1, 1, N)
        print(eat)
        update(eat, -1, 1, 1, N)
        nums[eat] += -1