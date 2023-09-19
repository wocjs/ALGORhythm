import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
tree = [[] for _ in range(n + 1)]

# 트리 구현
for _ in range(n-1):
    n1, n2, val = map(int, input().split())
    tree[n1].append([n2, val])
    tree[n2].append([n1, val])

# print(tree)    # [[], [[2, 3], [3, 2]], [[1, 3], [4, 5]], [[1, 2], [5, 11], [6, 9]], [[2, 5], [7, 1], [8, 7]], [[3, 11], [9, 15], [10, 4]], [[3, 9], [11, 6], [12, 10]], [[4, 1]], [[4, 7]], [[5, 15]], [[5, 4]], [[6, 6]], [[6, 10]]]


def dfs(x, wei):
    for _node, _val in tree[x]:
        if dist[_node] == -1:
            dist[_node] = wei + _val
            dfs(_node, wei + _val)


dist = [-1] * (n + 1)
dist[1] = 0
dfs(1, 0)
# print(dist)  # [-1, 0, 3, 2, 8, 13, 11, 9, 15, 28, 17, 17, 21]
start = dist.index(max(dist))

dist = [-1] * (n + 1)
dist[start] = 0
dfs(start, 0)
# print(dist)  # [-1, 28, 31, 26, 36, 15, 35, 37, 43, 0, 19, 41, 45]
print(max(dist))