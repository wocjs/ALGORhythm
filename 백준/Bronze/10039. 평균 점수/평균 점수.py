sm = 0
for _ in range(5):
    n = int(input())
    if n <= 40:
        n = 40
    sm += n
print(sm // 5)