
n, e = map(int, input().split())
arr = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(e):
	a, b = map(int, input().split())
	arr[a].append(b)
	arr[b].append(a)
cnt = 0
# print(arr)
# [[], [2, 5], [1, 5, 4, 3], [4, 2], [3, 6, 5, 2], [2, 1, 4], [4]]
for i in range(1, n+1):
	if not visited[i]:
		visited[i] = 1
		q = [i]
		cnt += 1
		while q:
			node = q.pop()
			for nde in arr[node]:
				if not visited[nde]:
					visited[nde] = 1
					q.append(nde)
	# print(visited)
print(cnt)