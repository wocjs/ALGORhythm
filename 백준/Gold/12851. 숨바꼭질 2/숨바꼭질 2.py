
# B12851
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
visited = [0] * 100001
ans, cnt = 0, 0
q = deque()
q.append(n)
while q:
	now = q.popleft()
	route_len = visited[now]
	if now == k:
		ans = route_len
		cnt += 1
		continue
	for nxt in [now-1, now+1, now*2]:
		if 0 <= nxt < 100001 and (not visited[nxt] or visited[nxt] == visited[now] + 1):
			visited[nxt] = visited[now] + 1
			q.append(nxt)
print(ans)
print(cnt)