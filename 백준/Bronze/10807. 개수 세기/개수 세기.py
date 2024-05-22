
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
cnt = 0
for i in range(n):
    if arr[i] == m:
        cnt += 1
print(cnt)