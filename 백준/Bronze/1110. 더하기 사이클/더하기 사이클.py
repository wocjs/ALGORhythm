
# B1110
n = input()
nm = n
cnt = 0
while True:
    cnt += 1
    if len(nm) == 1:
        nm = '0' + nm
    nxt = nm[-1]
    sm = 0
    for c in nm:
        sm += int(c)
    nxt += str(sm)[-1]
    nxt = str(int(nxt))
    # print(nxt)
    if nxt == n:
        break
    nm = nxt
print(cnt)