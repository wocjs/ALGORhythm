t = int(input())
for tc in range(t):
    arr = list(map(str, input().split()))
    for c in arr[1]:
        for _ in range(int(arr[0])):
            print(c, end='')
    print()