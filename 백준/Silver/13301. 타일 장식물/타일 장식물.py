n = int(input())
arr = [0] * 81
arr[0] = 4
arr[1] = 6
for i in range(2,n+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n-1])