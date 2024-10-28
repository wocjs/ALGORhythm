
import sys
input = sys.stdin.readline
X = 10007

def cal(x,n):
    if n == 1:
        return x
    cal2 = cal(x,n//2)
    if n%2:
        return cal2*cal2*x
    return cal2*cal2

def div(x,y):
  return x*cal(y, X - 2)%X

def comb(n, k):
    numor = 1
    denom = 1
    for i in range(k):
        numor = numor * (n-i) % X
        denom = denom * (i+1) % X
    return numor*cal(denom, 10007-2)%X


def Ncard(N):
    result = 0
    for i in range(1,N//4+1):
        result += comb(52-i*4, N-i*4) * comb(13, i)*((-1)**(i-1))
        result %= X
    return result

print(Ncard(int(input())))