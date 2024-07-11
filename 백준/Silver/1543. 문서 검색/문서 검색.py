
dc = input()
n = len(dc)
word = input()
m = len(word)
i = 0
cnt = 0
while i < n-m+1:
    if word == dc[i:i+m]:
        cnt += 1
        i += m
        continue
    i += 1
print(cnt)