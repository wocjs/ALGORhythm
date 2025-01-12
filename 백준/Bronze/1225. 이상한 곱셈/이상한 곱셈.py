n, m = input().split()
sm = 0
for i in n:
    for j in m:
        sm += int(i)*int(j)
print(sm)