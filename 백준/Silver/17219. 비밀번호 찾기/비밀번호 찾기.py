n, m = map(int, input().split())
dict = {}

for _ in range(n):
    site, passwd = input().split()
    dict[site] = passwd

for _ in range(m):
    print(dict[input()])