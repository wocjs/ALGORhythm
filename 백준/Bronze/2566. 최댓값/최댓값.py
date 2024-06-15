arr = [list(map(int, input().split())) for _ in range(9)]
mxVal, mxi, mxj = 0, 0, 0
for i in range(9):
    for j in range(9):
        if mxVal < arr[i][j]:
            mxVal = arr[i][j]
            mxi, mxj = i, j
print(mxVal)
print(mxi+1, mxj+1)