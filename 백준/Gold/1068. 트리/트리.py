
def dfs(del_node):
    tree[del_node] = -2
    for i in range(n):
        if del_node == tree[i]:
            dfs(i)


n = int(input())
tree = list(map(int, input().split()))
dnode = int(input())

dfs(dnode)

cnt = 0
for i in range(n):
    if tree[i] != -2 and i not in tree:
        cnt += 1
print(cnt)