n = int(input())
arr = [list(map(str, input().strip())) for _ in range(n)]
m = int(input())
if m == 1:
    for i in arr:
        print(''.join(i))
elif m == 2:
    for i in range(n):
        for j in range(n-1, -1, -1):
            print(arr[i][j], end='')
        print()
elif m == 3:
    for i in range(n-1, -1, -1):
        print(''.join(arr[i]))