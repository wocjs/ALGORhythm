import sys
n = int(input())
arr = list(map(int, input().split()))
_arr = arr[::-1]

inc = [1]*n
dec = [1]*n

for i in range(n):
	for j in range(i):
		#increase
		if arr[i] > arr[j]:
			inc[i] = max(inc[i], inc[j]+1)
		#decrease
		if _arr[i] > _arr[j]:
			dec[i] = max(dec[i], dec[j]+1)
# return reversed
dec = dec[::-1]

# find increase, decrease max
res = []
for i in range(n):
	res.append(dec[i] + inc[i] - 1)
# print(res)
print(max(res))