# B1546
n = int(input())
arr = list(map(int, input().split()))
mx = max(arr)
for i in range(n):
    arr[i] = arr[i] / mx*100
print(sum(arr) / n)