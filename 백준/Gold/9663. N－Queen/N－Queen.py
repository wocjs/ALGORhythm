
n = int(input())
arr = [0] * n
cnt = 0


def find(now):
    global cnt
    if now == n:
        cnt += 1
        return
    for i in range(n):
        arr[now] = i
        flag = True
        for j in range(now):
            if arr[now] == arr[j] or abs(now - j) == abs(arr[now] - arr[j]):
                flag = False
                break
        if flag:
            find(now + 1)
    pass


find(0)
print(cnt)