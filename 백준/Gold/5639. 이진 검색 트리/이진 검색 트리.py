import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

def post(st, en):
    if st > en:
        return
    mid = en + 1
    for i in range(st + 1, en + 1):
        if arr[i] > arr[st]:
            mid = i
            break
    post(st+1, mid-1)
    post(mid, en)
    print(arr[st])


post(0, len(arr) - 1)