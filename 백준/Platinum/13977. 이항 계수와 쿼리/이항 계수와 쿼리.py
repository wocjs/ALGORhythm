import sys
M = int(sys.stdin.readline())
p = 1000000007
factorial = [1]*4000001
for i in range(2,4000001): # 펙토리얼 구하기
    factorial[i] = (factorial[i-1]*i) % p
def find(x,n): # 제곱 구해주기
    if n == 1:
        return x % p
    else :
        temp = find(x,n//2)
        if n % 2 == 0:
            return temp*temp % p
        else:
            return temp*temp*x % p

for _ in range(M):
    N, R = map(int, sys.stdin.readline().split())
    print(factorial[N]*find(factorial[R]*(factorial[N-R]),p-2)%p) #이항계수 출력
