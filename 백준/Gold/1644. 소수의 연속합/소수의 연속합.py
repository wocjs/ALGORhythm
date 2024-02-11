
# B1644
# 에라토스테네스의 체 & 슬라이딩 윈도우
n = int(input())
X = n+1
arr = [1 for i in range(X)]
if n == 1:
    print(0)
    exit()

for i in range(2, X):
    if arr[i] == 1:
        now = i*2
        while now < X:
            arr[now] = 0
            now += i
anslst = []
for i in range(2, X):
    if arr[i]:
        anslst.append(i)
st, en = 0, 0
tmp_sm = anslst[st]
ans = 0
while en < len(anslst):
    #print(anslst)
    #print(st, en, tmp_sm)
    if tmp_sm == n:
        ans += 1
        en += 1
        if en < len(anslst):
            tmp_sm += anslst[en]
        else:
            break
    elif tmp_sm > n:
        tmp_sm -= anslst[st]
        st += 1
    else:
        en += 1
        if en < len(anslst):
            tmp_sm += anslst[en]
        else:
            break
    #print("ans :", ans)
print(ans)
