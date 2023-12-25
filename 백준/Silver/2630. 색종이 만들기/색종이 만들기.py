
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
w, b = 0, 0
def sol(x, y, n):
	global w
	global b
	
	# save start point
	color = arr[x][y]
	
	for i in range(x, x + n):
		for j in range(y, y + n):
			if color != arr[i][j]:
				# 하나라도 다르다?
				sol(x, y, n // 2)
				sol(x, y + n//2, n // 2)
				sol(x + n//2, y, n // 2)
				sol(x + n//2, y + n//2, n // 2)
				return
	if color == 0:
		w += 1
	else:
		b += 1
	

sol(0, 0, n)
print(w)
print(b)