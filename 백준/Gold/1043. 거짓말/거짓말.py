
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
know = set(map(int, input().split()[1:]))
arr = []
for _ in range(m):
	arr.append(set(map(int, input().split()[1:])))

for _ in range(m):	# 역순으로 이어져있으면 m만큼 되돌아와야 함
	for party in arr:
		if party & know:	# party 집합과 knowList의 교집합이 있는지 판단
			# knowList = knowList와 party의 합집합
			know = know.union(party)
			
cnt = m
for party in arr:
	if party & know:
		cnt -= 1
print(cnt)