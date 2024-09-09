
n, m = map(int, input().split())
m += 1
arr = [0]*m
for i in range(n, m):
    if i == 1:
        continue
    arr[i] = 1
for i in range(2, int(m**0.5)+1):
    idx = i*2
    while idx < m:
        arr[idx] = 0
        idx += i
for i in range(n, m):
    if arr[i]:
        print(i)
