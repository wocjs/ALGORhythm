n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
mx = 0
for i in range(n):
    if arr[i] > mx:
        cnt += 1
        mx = arr[i] + k
print(cnt)