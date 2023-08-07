
n = int(input())
ds = int(input())
arr = [int(input()) for _ in range(n-1)]

ans = 0
arr.sort()
if n == 1:
    print(0)
    exit(0)
while arr[-1] >= ds:
    ds += 1
    arr[-1] -= 1
    arr.sort()
    ans += 1
    # print(arr, ds)
print(ans)