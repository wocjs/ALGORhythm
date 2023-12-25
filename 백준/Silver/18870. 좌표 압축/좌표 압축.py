
n = int(input())
_arr = list(map(int, input().split()))
arr = sorted(list(set(_arr)))

dic = {arr[i] : i for i in range(len(arr))}
for i in _arr:
	print(dic[i], end=' ')
print()