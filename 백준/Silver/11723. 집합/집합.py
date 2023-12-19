import sys
input = sys.stdin.readline
t = int(input())
s = set()
for _ in range(t):
	order = list(input().split())
	# print(order)
	if len(order) > 1:
		msg, n = order
		num = int(n)
		if msg == 'add':
			s.add(num)
		elif msg == 'remove':
			try:
				s.remove(num)
			except:
				continue
		elif msg == 'check':
			if num in s:
				print(1)
			else:
				print(0)
		elif msg == 'toggle':
			if num in s:
				s.remove(num)
			else:
				s.add(num)
	else:
		msg = order[0]
		s = set()
		if msg == 'all':
			for i in range(1, 21):
				s.add(i)
		