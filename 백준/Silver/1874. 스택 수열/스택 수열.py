n = int(input())
cnt = 1
tmp = True
stack = []
op = []

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        op.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        print('NO')
        exit(0)
if tmp:
    for i in op:
        print(i)