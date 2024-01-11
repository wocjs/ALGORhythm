
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
mx = mn = arr
for _ in range(n-1):
    arr = list(map(int, input().split()))
    mx = [arr[0] + max(mx[0], mx[1]), arr[1] + max(mx), arr[2] + max(mx[1], mx[2])]
    mn = [arr[0] + min(mn[0], mn[1]), arr[1] + min(mn), arr[2] + min(mn[1], mn[2])]
print(max(mx), min(mn))