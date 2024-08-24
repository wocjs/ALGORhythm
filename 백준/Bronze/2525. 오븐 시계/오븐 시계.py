
n, m = map(int, input().split())
a = int(input())
m += a
while True:
    if m < 60:
        break
    m -= 60
    n += 1
while True:
    if n < 24:
        break
    n -= 24
print(n, m)