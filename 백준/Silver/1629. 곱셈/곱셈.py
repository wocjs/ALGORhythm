

'''
지수 법칙
A^m+n = A^m * A^n
나머지 분배 법칙
(A*B)%C = (A%C) * (B%C) % C
'''
a, b, c = map(int, input().split())
'''
10^11 % 12
= ((10^5)%12 x (10^5)%12 x 10)% 12
= ((10^2)%12 x (10^2)%12 x 10) %12 x
	 (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12

'''

def dfs(a, n):
	if n == 1:
		return a % c
	else:
		tmp = dfs(a, n//2)
		if n%2 == 0:
			return (tmp**2) % c
		else:
			return (a*tmp**2) % c


print(dfs(a, b))