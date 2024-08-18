n = int(input())
for _ in range(n):
    arr = list(map(str, input().split()))
    m = int(arr[0])
    print(arr[1][:m-1]+arr[1][m:])