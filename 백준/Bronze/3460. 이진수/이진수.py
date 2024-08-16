
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a = int(input())
    s = str(bin(a)[2:])[::-1]
    for i in range(len(s)):
        if s[i] == '1':
            print(i, end=' ')
    print()