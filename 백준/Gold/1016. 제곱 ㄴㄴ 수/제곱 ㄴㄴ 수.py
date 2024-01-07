mn, mx = map(int,input().split())
ans = mx - mn + 1
arr = [0] * (mx-mn+1)

for i in range(2, int(mx**0.5 + 1)):
    square = i**2
    for j in range((((mn-1)//square)+1)*square, mx+1, square):
        if not arr[j-mn]:
            arr[j-mn] = 1
            ans -= 1
print(ans)