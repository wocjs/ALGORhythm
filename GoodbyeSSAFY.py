import sys
sys.stdin = open('input.txt', 'r')
#####
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)
for i in arr:
    print(i)