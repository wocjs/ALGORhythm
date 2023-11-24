
n, k = map(int, input().split())

arr = [i+1 for i in range(n)]

print('<',end='')
while len(arr) > 1:
    for _ in range(k-1):
        arr.append(arr.pop(0))
    print(arr.pop(0), end=', ')
print(arr[-1], end='')
print(">")