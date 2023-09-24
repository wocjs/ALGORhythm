
n, m, l, k = map(int, input().split())
stars = []

for _ in range(k):
    a, b = map(int, input().split())
    stars.append([a, b])

ans = k
for x, _ in stars:
    for _, y in stars:
        tmp = k
        for a, b in stars:
            if x <= a <= x + l and y <= b <= y + l:
                tmp -= 1
        ans = min(ans, tmp)
print(ans)