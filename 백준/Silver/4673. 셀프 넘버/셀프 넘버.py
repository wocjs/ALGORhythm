nat = set(range(1, 10000))
gen = set()

for i in range(1, 10000):
    tmp = i
    for j in str(i):
        tmp += int(j)
    gen.add(tmp)
ans = sorted(nat - gen)
for i in ans:
    print(i)