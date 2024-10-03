
n = int(input())
m = n*2 - 1
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(m):
        print('*', end='')
    print()
    m -= 2
m = 3
for i in range(n-2, -1, -1):
    for j in range(i):
        print(' ', end='')
    for j in range(m):
        print('*', end='')
    print()
    m += 2
