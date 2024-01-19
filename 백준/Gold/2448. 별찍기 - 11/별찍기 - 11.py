
import sys
input = sys.stdin.readline
n = int(input())
stars = [[' ']*2*n for _ in range(n)]


def dfs(i, j, size):
	if size == 3:	# 기저조거ᄂ
		stars[i][j] = '*'
		stars[i+1][j-1] = stars[i+1][j+1] = '*'
		for k in range(-2, 3):
			stars[i+2][j+k] = '*'

	else:		# 아니며ᄂ 3배로 재구ᅵ ᄀᄀ
		newSize = size // 2
		dfs(i, j, newSize)
		dfs(i+newSize, j-newSize, newSize)
		dfs(i+newSize, j+newSize, newSize)


dfs(0, n-1, n)
for star in stars:
	print("".join(star))