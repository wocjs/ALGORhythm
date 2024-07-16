
cnt = 0
for _ in range(int(input())):
    _, d = map(str, input().split('-'))
    d = int(d)
    if d <= 90:
        cnt += 1
print(cnt)