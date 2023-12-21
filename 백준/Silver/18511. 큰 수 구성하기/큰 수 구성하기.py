n, k = map(int, input().split())
arr = list(map(int, input().split()))
l = len(str(n))
ans = 0

def dfs(num, len):
    global ans
    global l
    # print(num, len)
    if len >= 1:
        if int(num) <= n:
            ans = max(ans, int(num))
        if len >= l:
            return
    for char in arr:
        dfs(num+str(char), len+1)


dfs("", 0)
print(ans)