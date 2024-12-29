
n = list(map(int, input()))
a = 0
b = 0
line = len(n) // 2
for i in range(0,line):
    a += n[i]
for i in range(line, len(n)):
    b += n[i]

if a == b:
    print("LUCKY")
else:
    print("READY")