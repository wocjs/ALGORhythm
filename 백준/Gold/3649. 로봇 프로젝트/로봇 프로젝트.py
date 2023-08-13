
import sys

input = sys.stdin.readline

while True:
    try:
        size = int(input()) * 10**7
        n = int(input())
        arr = [int(input()) for _ in range(n)]
        arr.sort()
        p1, p2 = 0, n-1
        ans = [0, 0]
        while p1 < p2:
            if arr[p1] + arr[p2] == size:
                ans = [arr[p1], arr[p2]]
                break
            elif arr[p1] + arr[p2] < size:
                p1 += 1
            elif arr[p1] + arr[p2] > size:
                p2 -= 1
        # print(ans)
        if ans == [0, 0]:
            print('danger')
        else:
            print('yes', arr[p1], arr[p2])

    except:
        break
