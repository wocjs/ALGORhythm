
n = int(input())
for line in range(n-1):
    for i in range(line+1):
        print('*', end='')
    for i in range(2*n-(line*2+2)):
        print('', end=' ')
    for i in range(line+1):
        print('*', end='')
    print()
for _ in range(n*2):
    print('*', end='')
print()
for line in range(n-2, -1, -1):
    for i in range(line+1):
        print('*', end='')
    for i in range(2*n-(line*2+2)):
        print('', end=' ')
    for i in range(line+1):
        print('*', end='')
    print()