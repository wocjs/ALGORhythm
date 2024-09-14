
inp = list(map(int, input().split()))
ans = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(ans[i]-inp[i], end=' ')