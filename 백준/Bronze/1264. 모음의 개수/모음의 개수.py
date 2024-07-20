
lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    l = input()
    if l == '#':
        break
    cnt = 0
    for c in l:
        if c in lst:
            cnt += 1
    print(cnt)