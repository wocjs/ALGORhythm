
import sys

input = sys.stdin.readline

# depth층에서 가장 오른쪽(해당 층에서 최댓값)에 있는 노드 == S(n)
# a*(r^n-1)/(r-1) where a == 1 & r == k & n == depth
# -> (k**depth-1)//(k-1)
# def maxvalue(depth):
#     if depth <= 0:
#         return 0
#
#     return (k ** depth - 1) // (k - 1)

# 해당 노드의 depth 찾기
def depth_find(node):
    cnt = 1
    while node > 1:
        cnt += 1
        node = ((node - 2) // k) + 1
    return cnt
def find(a, b, ans):
    a_depth = depth_find(a)
    b_depth = depth_find(b)

    if a_depth < b_depth:
        a, b = b, a
        a_depth, b_depth = b_depth, a_depth

    while a_depth != b_depth:
        a = ((a - 2) // k) + 1
        a_depth -= 1
        ans += 1

    while a != b:
        a = ((a - 2) // k) + 1
        b = ((b - 2) // k) + 1
        ans += 2
    return ans


n, k, q = map(int, input().split())
for _ in range(q):
    x, y = map(int, input().split())
    if k == 1:
        print(abs(x - y))
        continue
    print(find(x, y, 0))
