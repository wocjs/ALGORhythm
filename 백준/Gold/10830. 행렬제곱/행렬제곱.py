# 10830
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def mul(mat1, mat2):
	res = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				res[i][j] += mat1[i][k] * mat2[k][j]
			res[i][j] %= 1000
	return res


def dev(_b, _arr):
	if _b == 1:
		return _arr
	elif _b == 2:
		return mul(_arr, _arr)
	else:
		tmp = dev(_b//2, _arr)
		if _b%2 == 0:
			return mul(tmp, tmp)
		else:
			return mul(mul(tmp, tmp), _arr)


n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = dev(b, arr)
for i in res:
	for num in i:
		print(num % 1000, end=' ')
	print()