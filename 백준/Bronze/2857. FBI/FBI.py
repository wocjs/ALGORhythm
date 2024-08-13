
cnt = 1
ans = False
while True:
    try:
        s = input()
        if 'FBI' in s:
            ans = True
            print(cnt, end=' ')
        cnt += 1
    except:
        break
if not ans:
    print("HE GOT AWAY!")
