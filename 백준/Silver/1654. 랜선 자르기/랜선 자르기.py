n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
st, en = 1, max(arr)

while st <= en:
    mid = (st + en) // 2
    lines = 0
    for i in arr:
        lines += i // mid
    if lines >= k:
        st = mid + 1
    else:
        en = mid - 1
print(en)