# B2166
n = int(input())
arr = []
for _ in range(n):
	arr.append(list(map(int, input().split())))
arr.append(arr[0])
ans = 0
for i in range(n):
	ans += arr[i][0] * arr[i+1][1]
	ans -= arr[i][1] * arr[i+1][0]
print(abs(ans/2))