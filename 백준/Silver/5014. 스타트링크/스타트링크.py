import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visited = [0] * (f+1)
visited[s] = 1
q = deque()
q.append([s, 0])
while q:
    now, cnt = q.popleft()
    if now == g:
        print(cnt)
        exit()
    for nxt in (now+u, now-d):
        if 0 < nxt <= f and not visited[nxt]:
            q.append([nxt, cnt+1])
            visited[nxt] = 1
print('use the stairs')