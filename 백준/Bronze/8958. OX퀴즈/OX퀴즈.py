
for tc in range(int(input())):
    ord = input()
    cnt = 1
    sm = 0
    for char in ord:
        if char == 'O':
            sm += cnt
            cnt += 1
        else:
            cnt = 1
    print(sm)