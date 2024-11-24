n = int(input())
for _ in range(n):
    arr = list(input().split())
    for word in arr:
        print(word[::-1], end=' ')
    print()