import sys
input = sys.stdin.readline

def chk(word):
    now = colors
    for i in range(len(word)):
        # 0까지 왔고, 뒷부분이 names에 있으면
        if now.get(0) and word[i:] in names:
            return True
        # 색깔이 가다가 끊기면
        if now.get(word[i]) is None:
            return False
        # 다음 알파벳으로 이동
        now = now[word[i]]
    return False


c, n = map(int, input().split())
colors = {}
for _ in range(c):
    now = colors
    for c in input().strip():
        if now.get(c) is None:
            now[c] = {}
        now = now[c]
    now[0] = 1  # {'r': {'e': {'d': {0: 1}}}
names = {input().strip() for _ in range(n)}

for _ in range(int(input())):
    print("Yes" if chk(input().strip()) else "No")
