
arr = [1] * 10001
for i in range(2,int(10000**0.5)+1):
    nm = i*2
    while nm < 10001:
        arr[nm] = 0
        nm += i
arr[0], arr[1] = 0, 0
n = int(input())
m = int(input())
sm = 0
mn = -1
for i in range(n, m+1):
    if arr[i]:
        sm += i
        if mn == -1:
            mn = i
if sm:
    print(sm)
print(mn)