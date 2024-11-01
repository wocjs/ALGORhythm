
def make_nine(N):
    while N % 10 != 9:
        for i in str(N):
            arr[int(i)] += num
        N -= 1
    return N


N = int(input())
arr = [0] * 10
num = 1
while N > 0:
    N = make_nine(N)
    if N < 10:
        for i in range(N+1):
            arr[i] += num
    else:
        for i in range(10):
            arr[i] += (N//10 + 1) * num
    arr[0] -= num
    num *= 10
    N //= 10
print(*arr)