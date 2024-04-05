pw = list(input().strip())
n = int(input())
fr = pw[:n]
bk = pw[-n:]
ans = 0
if len(pw)//2 >= n:
    for i in range(n):
        if fr[i] != bk[i]:
            ans += 1
else:
    k = len(pw)-n
    for i in range(k):
        p = i
        cnt = dict()
        while p < len(pw):
            if cnt.get(pw[p]):
                cnt[pw[p]] += 1
            else:
                cnt[pw[p]] = 1
            p += k

        m = max(cnt, key=cnt.get)
        for key in cnt.keys():
            if key == m:
                continue
            ans += cnt[key]
print(ans)