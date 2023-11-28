n = int(input())
ans = 0
while n >= 0:
    if n % 5 == 0:
        ans += n // 5
        break
    n -= 3
    ans += 1
if n < 0:
    ans = -1
print(ans)