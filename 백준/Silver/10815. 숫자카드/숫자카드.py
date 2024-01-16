import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
findarr = list(map(int, input().split()))

for now in findarr:
	low, high = 0, n-1
	ans = 0
	while low <= high:
		mid = (low + high) // 2
		
		if arr[mid] > now:
			high = mid - 1
		elif arr[mid] < now:
			low = mid + 1
		else:
			ans = 1
			break
	print(ans, end=" ")