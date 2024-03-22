t = int(input())
arr = [[0]*14 for _ in range(15)]

for i in range(14):
    arr[0][i] = i+1
for i in range(1, 15):
    for j in range(14):
        arr[i][j] = sum(arr[i-1][:j+1])

for tc in range(t):
    k = int(input())
    n = int(input())
    print(arr[k][n-1])