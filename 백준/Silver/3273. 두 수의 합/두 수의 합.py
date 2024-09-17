
n = int(input())
arr = sorted(list(map(int, input().split())))
s, e = 0, n-1
t = int(input())
cnt = 0
while s < e:
    sm = arr[s] + arr[e]
    if sm == t:
        cnt += 1
        s += 1
    elif sm < t:
        s += 1
    elif sm > t:
        e -= 1
print(cnt)