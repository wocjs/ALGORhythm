n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
ans = -1

for i in range(n-1, 0, -1):
    for j in range(i):
        # print(i, j)
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            cnt += 1
            if cnt == k:
                ans = f'{arr[j]} {arr[j+1]}'
                print(ans)
                exit(0)
print(ans)