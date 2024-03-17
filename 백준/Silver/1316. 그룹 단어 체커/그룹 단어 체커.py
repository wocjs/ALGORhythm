
# B1316
import sys
input = sys.stdin.readline
n = int(input())

ans = 0
for _ in range(n):
    st = input()
    a = set()
    flag = True
    a.add(st[0])
    for i in range(1, len(st)):
        if st[i] not in a:
            a.add(st[i])
        else:
            if st[i] == st[i-1]:
                continue
            else:
                flag = False
    if flag:
        ans += 1
        # print(st)
        # print(a)
print(ans)