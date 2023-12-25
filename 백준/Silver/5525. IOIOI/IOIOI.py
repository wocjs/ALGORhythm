n = int(input())
m = int(input())
s = input()
left, right = 0, 0
ans = 0

while right < m:
    if s[right:right+3] == 'IOI':
        right += 2
        if right - left == 2 * n:
            ans += 1
            left += 2
    else:
        right += 1
        left = right
print(ans)