from bisect import bisect_left
n = int(input())
arr = list(map(int, input().split()))
dp = [1]
x = [arr[0]]
for i in range(1, n):
	if arr[i] > x[-1]:
		dp.append(dp[-1] + 1)
		x.append(arr[i])
	else:
		idx = bisect_left(x, arr[i])
		x[idx] = arr[i]
print(dp[-1])