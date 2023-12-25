n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr = sorted(arr, key = lambda x : (x[0], x[1]))
for i in arr:
    print(*i)