import sys
input = sys.stdin.readline

def find(_nms):
    _nms.sort()
    for i in range(len(_nms) - 1):
        if _nms[i] in _nms[i + 1][0:len(_nms[i])]:
            print("NO")
            return
    print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(input().strip())
    find(nums)
