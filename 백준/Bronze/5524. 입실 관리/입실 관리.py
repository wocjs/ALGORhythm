
n = int(input())
for _ in range(n):
    word = input()
    for c in word:
        if c.isupper():
            print(c.lower(), end='')
        else:
            print(c, end='')
    print()