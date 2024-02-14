n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i > 1:
        for num in range(2, i):
            if i % num == 0:
                break
        else:
            cnt += 1
print(cnt)