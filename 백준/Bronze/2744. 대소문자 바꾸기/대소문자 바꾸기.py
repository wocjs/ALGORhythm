word = input()
for c in word:
    if c.islower():
        print(c.upper(), end='')
    else:
        print(c.lower(), end='')
print()