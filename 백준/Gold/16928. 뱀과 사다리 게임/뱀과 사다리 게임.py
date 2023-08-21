
n, m = map(int, input().split())
arr = [i for i in range(101)]
for _ in range(n + m):
    a, b = map(int, input().split())
    arr[a] = b
visited = [0] * 101
# print(arr)
q = [1]
visited[1] = 1
while q:
    now = q.pop(0)
    for i in range(1, 7):
        nxt = now + i
        if nxt > 100:
            continue

        cnt = arr[nxt]

        if not visited[cnt]:
            q.append(cnt)
            visited[cnt] = visited[now] + 1
            if cnt == 100:
                q = []
                break
        # print(visited)
print(visited[-1]-1)