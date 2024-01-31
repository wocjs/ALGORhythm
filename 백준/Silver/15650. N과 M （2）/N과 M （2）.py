from itertools import combinations
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
ans = set()
for st in combinations(arr, m):
	if st not in ans:
		ans.add(st)
ans = sorted(ans)
for i in ans:
	print(*i)