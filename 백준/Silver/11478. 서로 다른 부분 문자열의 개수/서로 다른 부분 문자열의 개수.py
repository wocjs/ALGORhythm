s = input()
n = len(s)
total = set()
for i in range(n):
    for j in range(i, n):
        total.add(s[i:j+1])

print(len(total))