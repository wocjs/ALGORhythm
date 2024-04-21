
n = int(input())
arr = list(map(int, input().split()))
ans = {}
for x in arr:
    if ans.get(x) is None:
        ans[x] = 1
    else:
        ans[x] += 1
m = int(input())
lst = list(map(int, input().split()))
for i in lst:
    if ans.get(i) is None:
        print(0, end=' ')
        continue
    print(ans[i], end=' ')
print()