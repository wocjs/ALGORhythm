
n = int(input())
arr = list(map(int, input().split()))
sm = 0
arr.sort()
for i in range(n+1):
	sm += sum(arr[0:i])
print(sm)