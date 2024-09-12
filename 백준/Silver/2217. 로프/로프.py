
n = int(input())
arr = []
res = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in range(n):
    res.append(arr[i] * (i + 1))
print(max(res))