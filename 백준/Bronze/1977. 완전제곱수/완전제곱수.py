
n = int(input())
m = int(input())+1
ans = []
for nm in range(n, m):
    if not nm**0.5 % 1:
        ans.append(nm)
if not ans:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))