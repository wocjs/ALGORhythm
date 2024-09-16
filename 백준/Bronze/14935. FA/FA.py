
s = input()
cnt = 0
while True:
    n = int(s[0]) * len(s)
    if n == int(s):
        print('FA')
        break
    s = str(n)
    cnt+=1
    if cnt == 10:
        print('NFA')
        break