
for _ in range(int(input())):
    s = input()
    print(s[0], end='')
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            continue
        print(s[i], end='')
    print()