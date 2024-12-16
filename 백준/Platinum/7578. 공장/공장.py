
import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
mapping = {val : (idx+1) for idx,val in enumerate(arr)}

arr_2 = list(map(int,sys.stdin.readline().split()))
converted = [mapping[arr_2[i]] for i in range(N)]

tree = [0]*(N+1)

def sumation(y):
    ans = 0
    while y>0:
        ans += tree[y]
        y -= (y&-y)

    return ans

def update(y):
    while y<len(tree):
        tree[y] += 1
        y += (y&-y)

ans = 0
for i in range(N):
    cur = converted[i]
    ans += (sumation(N) - sumation(cur))#ith 기계의 y값.
    update(cur)

print(ans)